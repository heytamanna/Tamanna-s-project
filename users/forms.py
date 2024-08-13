from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    profile_picture = forms.ImageField(required=False)
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email Id'}))
    address = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    city = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'City'}))
    state = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'State'}))
    pincode = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'placeholder': 'Pincode'}))
    user_type = forms.ChoiceField(choices=CustomUser.USER_TYPE_CHOICES, required=True, widget=forms.RadioSelect)

    class Meta:
        model = CustomUser
        fields = ('user_type','first_name', 'last_name', 'profile_picture', 'username', 'email','address', 'city', 'state', 'pincode','password1', 'password2',)
        widgets = {
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        }
