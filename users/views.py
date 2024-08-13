from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as AuthLoginView
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from .models import CustomUser

# Create your views here.


class UserSignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = '/login/'

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect('/dashboard/')

class CustomLoginView(AuthLoginView):
    template_name = 'registration/login.html'

@login_required
def dashboard(request):
    user = request.user
    print(f"User type: {user.user_type}")  
    if user.user_type == 'patient':
        return render(request, 'registration/patient_dashboard.html', {'user': user})
    elif user.user_type == 'doctor':
        return render(request, 'registration/doctor_dashboard.html', {'user': user})
    else:
        return redirect('/login/')
