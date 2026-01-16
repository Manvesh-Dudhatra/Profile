from django.contrib import admin
from .models import CustomUser

class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "password", "mobile", 'profile_image']
    
admin.site.register(CustomUser, UserAdmin)