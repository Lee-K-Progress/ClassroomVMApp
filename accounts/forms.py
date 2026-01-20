# Lee Kusowski
# Webhooks
# Dec 05 2025 

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AdminUserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Custom User Creation Form"""

    class Meta(UserCreationForm):
        model = CustomUser
        fields = {
            "username",
            "email",
        }


class CustomUserChangeForm(UserChangeForm):
    """Custom User Change Form"""

    class Meta:
        model = CustomUser
        fields = {
            "username",
            "email",
        }


class CustomAdminUserCreationForm(AdminUserCreationForm):
    """Custom User Creation Form"""

    class Meta(AdminUserCreationForm):
        model = CustomUser
        fields = {
            "username",
            "email",
        }