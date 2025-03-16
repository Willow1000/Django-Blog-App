from django.urls import path, include
from .views import *

urlpatterns = [
    path("",HomeView.as_view(),name="home"),
    path("signup/",RegistrationView.as_view(),name='registration'),
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',CustomLogoutView.as_view(next_page='login'),name='logout'),
    path("createblog",CreateBlogView.as_view(),name="createblog"),
    path('blogs/',ListBlogView.as_view(),name="blogs"),
    path("blog/<int:pk>/",BlogView.as_view(),name="blog"),
    path("delete/<int:pk>/",DeleteBlogView.as_view(),name = "delete"),
    path("update/<int:pk>/",UpdateblogView.as_view(),name="update")
]

from Django_Blog import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)