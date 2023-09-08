from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


# inherit UserCreationForm to create SignupForm
class SignupForm(UserCreationForm):
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id':"tel",
                "placeholder": "Enter your full name",
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'id':"email",
                "placeholder": "Enter your email",
            }
        )
    )
    phone_number = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'id':"password",
                "placeholder": "Enter your phone number",
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                
                "placeholder": "Enter your password",
                'id':"password",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id':"confirm-password",
                "placeholder": "Re-enter your password",
            }
        )
    )
    class Meta:
        model = User
        fields = ['fullname', 'email', 'phone_number', 'password1', 'password2']
        

# create a login form
class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                
                "placeholder": "Enter your email",
                "autocomplete":"email",
            }
        )
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "autocomplete":"password",
                "placeholder": "Enter your password",
            }
        )
    )
