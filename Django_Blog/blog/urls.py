from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"userApi",CustomUserViewSet,basename="userApi")
router.register(r"blogApi",BlogViewSet,basename ="blogApi")
router.register(r"commentApi",CommentViewSet,basename ="commentApi")

urlpatterns = [
    path("",HomeView.as_view(),name="home"),
    path("signup/",RegistrationView.as_view(),name='registration'),
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',CustomLogoutView.as_view(next_page='home'),name='logout'),
    path("createblog",CreateBlogView.as_view(),name="createblog"),
    path('blogs/',ListBlogView.as_view(),name="blogs"),
    path("blog/<int:pk>/",BlogView.as_view(),name="blog"),
    path("delete/<int:pk>/",DeleteBlogView.as_view(),name = "delete"),
    path("update/<int:pk>/",UpdateblogView.as_view(),name="update"),
    path("blog/<int:pk>/comment",CreateComment.as_view(),name="comment"),
    path("blog/<int:pk>/comments",Comments.as_view(),name="comments"),
    path("tag/<slug:tag_slug>/",TaggedBlogsView.as_view(),name="tags"),
    path("api/",include(router.urls))
]

from Django_Blog import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)