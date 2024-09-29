from django.urls import path

from users.views import UserRegistrationView, CustomUserLoginView,CustomUserLogoutView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', CustomUserLoginView.as_view(), name='login'),
    path('logout/', CustomUserLogoutView.as_view(), name='logout'),


]
