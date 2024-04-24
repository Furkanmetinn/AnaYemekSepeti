from django import forms
from .models import CustomUser

class LoginForm(forms.Form):
    username_or_email = forms.CharField(label='Kullanıcı Adı veya E-posta')
    password = forms.CharField(label='Şifre', widget=forms.PasswordInput)

    class Meta:
        model=CustomUser
        fields=['username','email','password','user_type']
