from django.shortcuts import redirect
from AnaYemekSepeti.account.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import CustomUser

def redirect_user(request):
    if request.user.is_authenticated:
        if request.user.user_type == CustomUser.CUSTOMER:
            return redirect('customer_dashboard')
        elif request.user.user_type == CustomUser.RESTAURANT_OWNER:
            return redirect('restaurant_owner_dashboard')
    else:
        return redirect('login')
    
def send_confirmation_email(user_email):
    subject = "Hesabınızı Onaylayın"
    message = (
        "Merhaba,\n\n"
        "Hesabınızı aktive etmek için aşağıdaki linke tıklayın:\n\n"
        "http://example.com/activate-account/\n\n"
        "Saygılarımla,\n"
        "Siteniz Ekibi"
    )
    from_email = "your@example.com"  # Gönderen e-posta adresi
    send_mail(subject, message, from_email, [user_email])   

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Kullanıcıyı pasif duruma getir
            user.save()
            user_email = form.cleaned_data.get('email')
            send_confirmation_email(user_email)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('signup_success')  # Kullanıcı kaydı başarılıysa yönlendirilecek URL
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def signup_success(request):
    return render(request, 'signup_success.html')