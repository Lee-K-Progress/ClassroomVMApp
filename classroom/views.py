"""
Lee Kusowski
ClassroomVMApp
3-5-2026
"""

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView

from .models import Classroom, Exercise, Task


class ClassroomListView(ListView):
    '''HOMEPAGE View'''

    model = Classroom
    template_name = "classroom_list.html"


class ClassroomUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''Classroom Update View'''

    model = Classroom
    template_name = "classroom_edit.html"
    success_url = reverse_lazy("classroom_list")
    fields = (
        "body",
    )

    def test_func(self):
        '''User should be Admin'''
# TODO: User should be Admin

class ClassroomDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''Classroom Delete View'''

    model = Classroom
    template_name = "classroom_delete.html"
    success_url = reverse_lazy("classroom_list")
    fields = (
        "body",
    )

    def test_func(self):
        '''User should be Admin'''
# TODO: User should be Admin


class ClassroomCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """Classroom Create View"""

    model = Classroom
    template_name = "classroom_create.html"
    success_url = reverse_lazy("classroom_list")
    fields = (
        "body",
    )

    def test_func(self):
        '''User should be Admin'''
# TODO: User should be Admin


class ClassroomDetailExerciseListView(LoginRequiredMixin, View):
    '''Classroom Detail / Exercise List View'''

    model = Classroom
    template_name = "classroom_detail_exercise_list.html"


class ExerciseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Exercise Update View"""

    model = Exercise
    template_name = "exercise_edit.html"
    success_url = reverse_lazy("classroom_detail_exercise_list")
    fields = (
        "body",
    )

    def test_func(self):
        '''User should be Admin'''
# TODO: User should be Admin


class ExerciseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Exercise Delete View"""

    model = Exercise
    template_name = "exercise_delete.html"
    success_url = reverse_lazy("classroom_detail_exercise_list")

    def test_func(self):
        '''User should be Admin'''
# TODO: User should be Admin


class ExerciseCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """Exercise Create View"""

    model = Exercise
    template_name = "exercise_new.html"
    success_url = reverse_lazy("classroom_detail_exercise_list")
    fields = (
        "body",
    )

    def test_func(self):
        '''User should be Admin'''
# TODO: User should be Admin

    def form_valid(self, form):
        """
        Form Valid:
        - User is Author or Superuser
        - Exercise has a description
        - Exercise has URL
        - VM URL is available
        """

        form.instance.author = self.request.user
# TODO: Form Valid Exercise
        return super().form_valid(form)


class ExerciseDetailTaskListSubmissionCreateView(View):
    '''
    Exercise Detail / Task List / Submission Create View
    List of Tasks through Submission Subclassing
    Submission Form Create
    '''

    model = Exercise
    template_name = "exercise_detail_task_list.html"


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Task Update View"""

    model = Task
    template_name = "task_edit.html"
    success_url = reverse_lazy("task_list")
    fields = (
        "body",
        "image_url",
    )

    def test_func(self):
        '''User should be Admin'''
# TODO: User should be Admin


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Task Delete View"""

    model = Task
    template_name = "task_delete.html"
    success_url = reverse_lazy("task_list")

    def test_func(self):
        '''User should be Admin'''
# TODO: User should be Admin


class TaskCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """Task Create View"""

    model = Task
    template_name = "task_new.html"
    success_url = reverse_lazy("task_list")
    fields = (
        "body",
        "image_url",
    )

    def test_func(self):
        '''User should be Admin'''
# TODO: User should be Admin

    def form_valid(self, form):
        """
        Form Valid:
        - User is Author or Superuser
        - Task has a Flag
        """

        form.instance.author = self.request.user
# TODO: Form Valid Task
        return super().form_valid(form)


class ExerciseDetailSubmissionListView(LoginRequiredMixin, View):
    '''List View of All Submissions for a Single Exercise'''

    model = Exercise
    template_name = "exercise_detail_submission_list.html"


class SubmissionDetailView(LoginRequiredMixin, View):
    '''Submission Detail View'''

    model = Exercise
    template_name = "submission_detail.html"


class StudentListView(LoginRequiredMixin, View):
    '''Roster of Students in a Class with Grades'''

    model = Classroom
    template_name = "student_list.html"