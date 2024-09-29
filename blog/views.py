from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DeleteView, DetailView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import BlogPost
from blog.serializers import BlogPostSerializer, CustomUserSerializer
from users.models import CustomUser


# Create your views here.


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_homepage.html'
    context_object_name = 'posts'
    paginate_by = 3
    ordering = ['-created_at']


class UserProfileView(TemplateView,LoginRequiredMixin):
    template_name = 'blog/profile.html'


class BlogPage(TemplateView,LoginRequiredMixin):
    template_name = 'blog/blogs_page.html'

class BlogPostCreateView(APIView):
    template_name = 'blog/add_blogs.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):

        if not request.user.is_authenticated:
            return redirect('login')  # Redirect to login page if not authenticated

        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)  # Set the author to the current user
            return redirect('add_blog_post')  # Redirect after successful creation


        return render(request, self.template_name, {'serializer': serializer})





class ProfileUpdateView(LoginRequiredMixin, APIView):
    def get(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)

        return render(request, 'blog/profile_update.html', {'user': user})

    def post(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        serializer = CustomUserSerializer(user, data=request.data, partial=True)  # Allow partial updates

        if serializer.is_valid():
            serializer.save()

            return redirect(reverse('profile', kwargs={'pk': user.pk}))  # Adjust 'user-profile' to match your URL name
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserBlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'blog_posts'

    def get_queryset(self):
        return BlogPost.objects.filter(author=self.request.user)


class BlogPostUpdateView(APIView):
    def get(self, request, pk):
        blog_post = get_object_or_404(BlogPost, pk=pk)
        serializer = BlogPostSerializer(blog_post)
        return render(request, 'blog/update_blogPost.html', {'blog_post': serializer.data})

    def post(self, request, pk):
        blog_post = get_object_or_404(BlogPost, pk=pk)
        serializer = BlogPostSerializer(blog_post, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return redirect('blogList')  # Adjust as needed for your URL name


        return render(request, 'blog/update_blogPost.html', {'blog_post': serializer.data, 'errors': serializer.errors})


class BlogPostDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    success_url = reverse_lazy('blogList')

    def get_queryset(self):

        return BlogPost.objects.filter(author=self.request.user)

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_singlepage.html'
    context_object_name = 'blog_post'


