# arachne-2026
A custom, Django-based, front end for a virtual lab environment.

## Author

Lee Kusowski

## Description

PRODUCTION ONLY

The Classroom Lab App is a django-based web app meant to support access to
virtual machines (VM's) to suppliment CIS course materials. SSO support requested.

    Users can:
Signup & Login
Be members of a Classroom
View a Classroom's Exercises
Open permitted Exercises
    View Exercises, Tasks
    Create Submissions

    Instructors can:
Create Classes
Create Exercises
Create Tasks

    Admin can:
CRUD for Users


## Dev Guide

    Users:
AbstractBase class with subclassing:
    1. Created a new class called CustomUser that subclasses AbstractUser
    2. Removed the username field
    3. Made the email field required and unique
    4. Set the USERNAME_FIELD -- which defines the unique identifier for the User model -- to email
    5. Specified that all objects for the class come from the CustomUserManager


## Resources Used

Django CustomUser Guide:
https://testdriven.io/blog/django-custom-user-model/


Django Package for Microsoft SSO Authentication:
https://django-microsoft-auth.readthedocs.io/en/latest/

