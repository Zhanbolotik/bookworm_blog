from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from .forms import RegistrationForm
from .models import User

class RegisterView(CreateView):
    model = User
    template_name = 'account/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')

class SignInView(LoginView):
    template_name = 'account/login.html'


def profile(request):
    return render(request, 'account/profile.html')




