from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', front_page.home, name='home'),
    path('courses/', front_page.courses, name='courses'),
    path('about/', front_page.about, name='about'),
    path('contact/', front_page.contact, name='contact'),
    path('cart/', front_page.cart, name='cart'),
    path('login/', user_management.loginPage, name='login'),
    path('signup/', user_management.signup, name='signup'),
    path('logout/', user_management.logoutUser, name='logout'),
    path('activate-user/<uidb64>/<token>', user_management.activate_user, name='activate'),
    
    path(
        'reset_password/', 
        auth_views.PasswordResetView.as_view(template_name="password/password_reset.html"), 
        name='password_reset'
    ),
    path(
        'reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password/password_reset_sent.html"), 
        name='password_reset_done'),
    path(
        'reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_form.html"), 
        name='password_reset_confirm'),
    path(
        'reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password/password_reset_done.html"), 
        name='password_reset_complete'),
]