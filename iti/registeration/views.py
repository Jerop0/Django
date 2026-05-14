from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic
from django.urls import reverse_lazy


def home(request):
    return render(request, "registeration/registeration.html")


class UserLogin(LoginView):
    template_name = 'registeration/registeration_login.html'
    next_page = reverse_lazy('Registeration')


class UserLogout(LogoutView):
    next_page = reverse_lazy('Registeration')


class Register(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registeration/registeration_signup.html'
    success_url = reverse_lazy('Registeration_Login')
