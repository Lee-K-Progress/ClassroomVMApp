"""
Lee Kusowski
ClassroomVMApp
3-5-2026
"""

from django.db import models
from django.conf import settings


class Classroom(models.Model):
    '''Model for Classroom'''

    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name = "classrooms",
        on_delete = models.CASCADE,
    )

    class_name = models.CharField(max_length=50)
    crn = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        '''Set string to return when refering to an instance'''

        return str(self.class_name)


class Exercise(models.Model):
    '''Model for Exercise'''

    classroom = models.ForeignKey(
        Classroom,
        related_name = "exercises",
        on_delete=models.CASCADE,
        )

    exercise_name = models.CharField(max_length=50)
    vm_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(auto_now = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        '''Set string to return when refering to an instance'''

        return str(self.exercise_name)

class Task(models.Model):
    '''Model for Task'''

    exercise = models.ForeignKey(
        Exercise,
        related_name = "tasks",
        on_delete = models.CASCADE,
    )
    task_name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    total_points = models.IntegerField()
    flag = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        '''Set string to return when refering to an instance'''

        return str(self.task_name)

class Submission(Exercise):
    '''Model for Submission'''

    task = models.ForeignKey(
        Task,
        related_name = "submission",
        on_delete = models.CASCADE,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name = "submissions",
        on_delete = models.CASCADE,
    )

    earned_points = models.IntegerField()
    input_flag = models.TextField(blank=True)
    submitted = models.DateTimeField(auto_now_add = True)
