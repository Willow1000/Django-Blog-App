from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView,ListView,DetailView,UpdateView,DeleteView
from .forms import SignUpForm,LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView ,LogoutView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import *
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


class CreateBlogView(LoginRequiredMixin,CreateView):
    model = Blog
    fields = ["category","Title",'Cover_image',"Content"]
    template_name = "createblog.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        return self.request.user.role == "blogger" or self.request.user.role == "admin" 
    
    def form_valid(self, form):
        form.instance.Blogger = self.request.user
        return super().form_valid(form)

class ListBlogView(ListView):
    model = Blog
    template_name = "blogs.html"
    context_object_name = 'blogs'

class BlogView(DetailView):
    model=Blog
    template_name="blog.html"
    context_object_name="blog"    

class DeleteBlogView(DeleteView):
    model=Blog
    template_name="blog.html"
    context_object_name="blog"
    success_url = reverse_lazy('blogs')  

class UpdateblogView(UpdateView):
    model = Blog
    template_name="updateblog.html"   
    success_url = reverse_lazy("blogs") 
    fields = ["Title","Cover_image","Content",'category']
    context_object_name='record'