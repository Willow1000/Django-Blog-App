from django.contrib import admin
from .models import CustomUser,Blog


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username"]
    list_filter = ["username","email"]
    search_fields = ["username","email"]

class BlogAdmin(admin.ModelAdmin):
    ist_display = ["Title"]
    list_filter = ["Title","category"]
    search_fields = ["Title","category"]
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Blog,BlogAdmin)