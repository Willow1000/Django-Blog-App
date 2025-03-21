
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

# Check if objects exist
# print(OutstandingToken.objects.all())  # Should not raise an error if migrations are correct


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('blog.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
