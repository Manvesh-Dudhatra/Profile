from django.contrib import admin
from .models import CustomUser, Inquiry

class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "password", "mobile"]

class InquiryAdmin(admin.ModelAdmin):
    list_display = ["name", "cname", "address", "email","phone", "message"]

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Inquiry, InquiryAdmin)
