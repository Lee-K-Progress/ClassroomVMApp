# Lee Kusowski
# Webhooks
# Dec 05 2025

from django.urls import path
from .views import SignUpView, AccountDetailView, AccountUpdateView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("<int:id>/", AccountDetailView.as_view(), name="account_detail"),
    path("edit/<int:pk>/", AccountUpdateView.as_view(), name="account_edit"),
]
