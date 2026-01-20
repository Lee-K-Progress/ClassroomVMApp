# Lee Kusowski
# Webhooks
# Dec 05 2025

from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUpView(CreateView):
    """Sign Up View"""

    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class AccountDetailView(LoginRequiredMixin, DetailView):
    '''Account Detail View'''

    model = CustomUser
    template_name = "account_detail.html"
    pk_url_kwarg = "id"

class AccountUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''Account Edit View'''

    model = CustomUser
    fields = (
        "username",
        "first_name",
        "last_name",
        "email",
    )
    template_name = "account_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.username == self.request.user.username