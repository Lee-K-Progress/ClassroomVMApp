# Lee Kusowski
# ClassroomVMApp
# 3-8-2026

from django.contrib import admin

from .models import Classroom, Exercise, Task


class TaskInLine(admin.StackedInline):
    """Inline of Tasks"""
    model = Task

class ExerciseAdmin(admin.ModelAdmin):
    """Admin View for Exercises"""
    inlines = [
        TaskInLine,
    ]

class ExerciseInLine(admin.StackedInline):
    """Inline of Exercise"""
    model = Exercise

class ClassroomAdmin(admin.ModelAdmin):
    '''Admin View for Classrooms'''
    inlines = [
        ExerciseInLine,
    ]


admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Task)
