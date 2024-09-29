from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.views import View

from rest_framework.views import APIView

from users.serializers import CustomUserRegistrationSerializer


# Create your views here.

class UserRegistrationView(APIView):

    def get(self, request):
        serializer = CustomUserRegistrationSerializer()
        return render(request, 'user_register.html', {'serializer': serializer})

    def post(self, request):
        print("Received registration data:", request.data)
        serializer = CustomUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            print("Serializer data is valid.")
            try:
                user = serializer.save()
                print("User created successfully:", user)
                return redirect('login')
            except Exception as e:
                print("Error saving user:", str(e))
        else:
            print("Serializer errors:", serializer.errors)
        return render(request, 'user_register.html', {'serializer': serializer})

class CustomUserLoginView(View):
    template_name = 'user_login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):

        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            return HttpResponseRedirect(reverse('homepage'))  # Replace 'homepage' with the actual name of your homepage URL pattern
        else:

            messages.error(request, "Invalid username or password")
            return render(request, self.template_name)




class CustomUserLogoutView(View):
    def get(self, request, *args, **kwargs):

        logout(request)

        return redirect(reverse('homepage'))

