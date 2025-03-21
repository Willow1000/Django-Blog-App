from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.contrib.auth.base_user import BaseUserManager
from django.utils.timezone import now
from taggit.managers import TaggableManager


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

    # likes = models.ForeignKey(Like,on_delete=models.CASCADE)
    def __str__(self):
        return self.username
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
    Content = models.TextField(max_length=5000)
    Cover_image = models.ImageField(upload_to='blog_images/', blank=True,null=True)
    Blogger = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="blogger")
    tags = TaggableManager()
    Likes = models.PositiveIntegerField(default=0)
    Relevant_links = models.JSONField(blank=True,null=True)

    def __str__(self):
        return self.Title
    
    
class Like(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)    
class Comment(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)