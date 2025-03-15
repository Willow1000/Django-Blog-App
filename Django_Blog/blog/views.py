from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView
from .forms import SignUpForm,LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView ,LogoutView
from django.contrib.auth import logout
# Create your views here.

class RegistrationView(CreateView):
    form_class = SignUpForm
    template_name = "register.html"
    success_url = reverse_lazy('home')

class HomeView(TemplateView):
    template_name = 'home.html'


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    # redirect_authenticated_user = True
    next_page= reverse_lazy('home')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("login")    
    def dispatch(self, request, *args, **kwargs):
        logout(request)  # Ensure session is cleared
        return redirect(self.next_page)
