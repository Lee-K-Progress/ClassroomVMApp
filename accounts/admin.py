# Lee Kusowski
# Webhooks
# Dec 05 2025 

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomAdminUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """Custom User Admin, Registers CustomUser model in admin"""

    add_form = CustomAdminUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "is_staff",
    ]
    # fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("date_of_birth",)}),)
    # add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("date_of_birth",)}),)


admin.site.register(CustomUser, CustomUserAdmin)