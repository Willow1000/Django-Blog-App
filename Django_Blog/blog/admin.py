from django.contrib import admin
from .models import CustomUser


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username"]
    list_filter = ["username","email"]
    search_fields = ["username","email"]

admin.site.register(CustomUser,CustomUserAdmin)