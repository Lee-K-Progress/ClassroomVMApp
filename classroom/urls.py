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
    ExerciseDetailTaskListSubmissionCreateView
    )

urlpatterns = [
    path(
        "<int:pk>/<int:crn>/",
        ClassroomDetailExerciseListView.as_view(),
        name="classroom_detail_exercise_list",
        ),
    path(
        "<int:pk>/attempt",
        ExerciseDetailTaskListSubmissionCreateView.as_view(),
        name="exercise_detail_task_list_submission_create",
    ),
    path("classrooms/", ClassroomListView.as_view(),
         name="classroom_list"),
    path('', RedirectView.as_view(pattern_name="classroom_list")),
]
