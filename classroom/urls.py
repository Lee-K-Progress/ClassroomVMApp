"""
Lee Kusowski
ClassroomVMApp
3-5-2026
"""

from django.urls import path
from django.views.generic import RedirectView

from .views import (
    ClassroomListView,
    ClassroomDetailExerciseListView,
    SubmissionCreateExerciseDetailTaskListView
    )

urlpatterns = [
    path(
        "<int:pk>/<int:crn>/",
        ClassroomDetailExerciseListView.as_view(),
        name="classroom_detail_exercise_list",
        ),
    path(
        "<int:pk>/attempt",
        SubmissionCreateExerciseDetailTaskListView.as_view(),
        name="submission_create_exercise_detail_task_list",
    ),
    path("classrooms/", ClassroomListView.as_view(),
         name="classroom_list"),
    path('', RedirectView.as_view(pattern_name="classroom_list")),
]
