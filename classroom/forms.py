"""
Lee Kusowski
ClassroomVMApp
4-12-2026
"""

from django import forms

from .models import Submission


class SubmissionForm(forms.ModelForm):
    """Submission Form"""

    class Meta:
        model = Submission
        fields = {"input_flag"}