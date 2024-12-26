from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

class CustomAuthenticationForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        label='Username',
        widget=forms.TextInput(attrs={
            'class': 'custom-input',
            'placeholder': 'Enter your username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'custom-input',
            'placeholder': 'Enter your password'
        }),
        label='Password'
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            # Authenticate the user
            user = authenticate(username=username, password=password)
            if user is None:
                raise ValidationError("Invalid username or password")
        return cleaned_data

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Optionally, you can add custom field labels and help texts here

    # Remove or customize the help texts for password fields
    username = forms.CharField(
        max_length=150, 
        help_text=None,
        label="Enter your username",
        widget=forms.TextInput(attrs={'class': 'custom-input'})
    )
    email = forms.CharField(
        max_length=150, 
        help_text=None,
        label="Enter your Email",
        widget=forms.EmailInput(attrs={'class': 'custom-input'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'custom-input'}),
        label="Enter your Password",
        help_text=None
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'custom-input'}),
        label="Re-Enter your Password",
        help_text=None
    )
