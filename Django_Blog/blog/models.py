from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.contrib.auth.base_user import BaseUserManager
from django.utils.timezone import now

# Create your models here.
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
    
class CustomUser(AbstractUser):
    ROLE_CHOICES = (('Admin',"admin"),
                    ("Blogger","blogger"),
                    ("Viewer","viewer"))
    
    role = models.CharField(max_length=50,choices=ROLE_CHOICES,default="Viewer")
    objects = CustomUserManager()   
    user_permissions = models.ManyToManyField(Permission,related_name="customuser_permission")
    groups = models.ManyToManyField(Group,related_name="customuser_group")


class Like(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    time = models.DateTimeField(default=now)

class Comment(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    time = models.DateTimeField(default=now)
    likes = models.ForeignKey(Like,on_delete=models.CASCADE)

class Blog(models.Model):
    CATEGORY_CHOICES = (("Beauty","beauty"),
                        ("Lifestyle","lifestyle"),
                        ("Food","food"),
                        ("Finance","finance"),
                        ("Relationships","relationsships"),
                        ("Career",'career'))
    Time = models.DateTimeField(default=now)
    category = models.CharField(max_length=100,choices=CATEGORY_CHOICES)
    Title = models.CharField(max_length=250)
    Cover_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    Blogger = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    Likes = models.ForeignKey(Like,on_delete=models.CASCADE)
    Comments = models.ForeignKey(Comment,on_delete=models.CASCADE)
