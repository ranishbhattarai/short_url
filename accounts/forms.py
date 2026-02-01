from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


# this is a django form for user registration
class RegisterForm(UserCreationForm):
    # here we can add more fields if needed, I added email
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={
                                 'class': 'w-full px-4 py-3 bg-slate-800 border border-white/10 rounded-lg text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500',
                                 'placeholder': 'Enter your email'
                             }))

    # meta class to specify model and fields, we are using CustomUser model and fields username, email, password1, password2.
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-slate-800 border border-white/10 rounded-lg text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Choose a username'
            }),
        }
        labels = {
            'username': 'Username',
        }
    # customizing the init method to add classes and placeholders to password fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'w-full px-4 py-3 bg-slate-800 border border-white/10 rounded-lg text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Create a password'
        })
        self.fields['password1'].help_text = 'Your password must be at least 8 characters.'
        
        self.fields['password2'].widget.attrs.update({
            'class': 'w-full px-4 py-3 bg-slate-800 border border-white/10 rounded-lg text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Confirm your password'
        })
        self.fields['password2'].help_text = 'Enter the same password again for verification.'
        
        # Optional: customize other field help text
        self.fields['username'].help_text = 'Letters, digits and @/./+/-/_ only.'

 # customizing login form inheriting from AuthenticationForm 
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 bg-slate-800 border border-white/10 rounded-lg text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 bg-slate-800 border border-white/10 rounded-lg text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Password'
        })
    )

      


    