# LESSONS
<!-- 1 Testing Functions that require authentication -->

when creating an instance of the user, .set_password for setting the password then .save() the instance

<!-- When creating forms -->

set enctype="multipart/form-data" if you want your form to accept image input

<!-- Reversing registered routes -->

when you register your urls using routers, use basename-list for multiple instances i.e viewing multiple comments or basename-detail for viewing a single comment


<!-- AUTH -->
# JWT
<!-- settings.py -->
INSTALLED_APPS = [
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist', 
]
https://dev.to/ki3ani/implementing-jwt-authentication-and-user-profile-with-django-rest-api-part-3-3dh9

https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',  # Ensure this is present
    ),
    'DEFAULT_AUTHENTICATION_CLASSES':
      [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        
    ]
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=180),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=50),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',

    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}
<!-- PROJECT urls.py -->
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

URLPATTERNS = [
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
# SESSION
SESSION_COOKIE_AGE = 60  # 1 hour
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


<!-- URLS -->
# URLS
STATIC_URL = 'static/'
MEDIA_ROOT = os.path.join(BASE_DIR,"media")
MEDIA_URL='/media/'
LOGIN_URL = 'login/'


# Signals
from django.db.models.signals import "insert type of signal"
from django.dispatch import receiver

<!-- Apps.py -->
def ready(self):
    from .signals import "signal"


# MAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = "wilkinsondari7@gmail.com"
EMAIL_HOST_PASSWORD = "vsgc hjli dvhl ahwv"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False


# ALLAUTH
<!-- settings.py -->
INSTALLED_APPS :"allauth","allauth.account","allauth.socialaccount",'allauth.socialaccount.providers.google'...

OPTIONS IN TEMPLATES :'django.template.context_processors.request'

AUTHENTICATION_BACKENDS: "allauth.account.auth_backends.AuthenticationBackend"

SOCIALACCOUNT_PROVIDERS: "google":{
    "APP":{
        "client_id":,
        "secret":,
        "key":,
    }
}

urlpatterns: path("accounts/",include("allauth.urls))


# CustomUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates and returns a regular user with the given email and password."""
        if not email:
            raise ValueError("The Email field must be set")
        
        email = self.normalize_email(email)  # Normalize email (lowercase)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Hash password
        user.save(using=self._db)  # Save to database
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Creates and returns a superuser with all permissions."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)



