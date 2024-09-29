from django.urls import path
from blog.views import BlogPostListView, UserProfileView, BlogPage, BlogPostCreateView, ProfileUpdateView, \
    UserBlogPostListView, BlogPostUpdateView, BlogPostDeleteView, BlogDetailView

urlpatterns = [
    path('', BlogPostListView.as_view(), name='homepage'),
    path('profile<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('BlogPage/', BlogPage.as_view(), name='BlogPage'),
    path('addblog/', BlogPostCreateView.as_view(), name='add_blog_post'),
    path('profile/update/<int:pk>/', ProfileUpdateView.as_view(), name='profile-update'),
    path('blogList/', UserBlogPostListView.as_view(), name='blogList'),
    path('blog/update/<int:pk>/', BlogPostUpdateView.as_view(), name='blogupdate'),
    path('blog/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='delete_blog_post'),
    path('blogsinglepage/<int:pk>/', BlogDetailView.as_view(), name='blogsinglepage'),
]
