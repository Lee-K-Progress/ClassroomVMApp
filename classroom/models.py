from django.db import models
from django.conf import settings


class Classroom(models.Model):
    '''Model for Classroom'''

    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name = "instructor",
        on_delete=models.CASCADE,
    )

    classname = models.TextField()
    crn = models.IntegerField()
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        '''Set string to return when refering to an instance'''

        return str(self.classname)
    

class Exercise(models.Model):
    '''Model for Exercise'''

    classroom = models.ForeignKey(
        Classroom,
        related_name = "exercises",
        on_delete=models.CASCADE,
        )
    
    # instructor = models.ForeignKey(
    #     settings. AUTH_USER_MODEL,
    #     related_name = "exercises",
    #     on_delete= models.CASCADE,
    # )

    vm_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField()


class Task(models.Model):
    '''Model for Task'''

    exercise = models.ForeignKey(
        Exercise,
        related_name = "tasks",
        on_delete = models.CASCADE,
    )

    description = models.TextField(blank=True)
    # max_points = models.IntegerField()
    flag = models.TextField()
    created = models.DateTimeField()


class Submission(models.Model):
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
    created = models.DateTimeField(auto_now_add = True)
