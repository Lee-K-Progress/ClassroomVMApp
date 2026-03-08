# Lee Kusowski
# ClassroomVMApp
# 3-8-2026

from django.contrib import admin

from .models import Classroom, Exercise


class ExerciseInLine(admin.StackedInline):
    model = Exercise


class ClassroomAdmin(admin.ModelAdmin):
    '''Admin View for Classroom'''
    inlines = [
        ExerciseInLine,
    ]


admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Exercise)
