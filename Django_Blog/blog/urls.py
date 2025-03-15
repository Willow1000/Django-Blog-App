from django.urls import path, include
from .views import *

urlpatterns = [
    path("",HomeView.as_view(),name="home"),
    path("signup/",RegistrationView.as_view(),name='registration'),
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',CustomLogoutView.as_view(next_page='login'),name='logout')

]