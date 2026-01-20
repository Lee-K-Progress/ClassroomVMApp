from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView

from .models import Classroom, Exercise


class ClassroomListView(ListView):
    '''HOMEPAGE View'''

    model = Classroom
    template_name = "classroom_list.html"


class ClassroomDetailExerciseListView(View):
    '''Classroom Detail / Exercise List View'''

    model = Classroom
    template_name = "classroom_detail_exercise_list.html"
    
    
class ExerciseDetailTaskListView(View):
    '''Exercise Detail / Task List View'''

    model = Exercise
    template_name = "exercise_detail_task_list.html"


class ExerciseDetailSubmissionListView(View):
    '''List View of All Submissions for a Single Exercise'''

    model = Exercise
    template_name = "exercise_detail_submission_list.html"


class SubmissionDetailView(View):
    '''Submission Detail View'''

    model = Exercise
    template_name = "submission_detail.html"


class StudentListView(View):
    '''Roster of Students in a Class with Grades'''

    model = Classroom
    template_name = "student_list.html"