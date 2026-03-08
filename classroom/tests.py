"""
Lee Kusowski
ClassroomVMApp
3-5-2026
"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Classroom, Exercise

class ClassroomTests(TestCase):
    """Classroom Tests"""

    @classmethod
    def setUpTestData(cls):
        """Set Up Test Data"""

        cls.instructor = get_user_model().objects.create_user(
            email = "instructor@fakeemail.com",
            password = "verysecret",
        )

        cls.classroom = Classroom.objects.create( # PYLINT FALSE POSITIVE?
            instructor = cls.instructor,
            class_name = "Test Class",
            crn = "99999999",
            description = "Test Classroom Description",
        )

        cls.exercise = Exercise.objects.create( # PYLINT FALSE POSITIVE?
            classroom = cls.classroom,
            exercise_name = "Test Exercise",
            vm_url = "test.url",
            description = "Test Exercise Description",
        )

    ## Model Tests ##
    def test_classroom_model(self):
        """Test Classroom Model"""
        # Fields
        self.assertEqual(self.classroom.class_name, "Test Class")
        self.assertEqual(self.classroom.crn, "99999999")
        self.assertEqual(self.classroom.description, "Test Classroom Description")
        # Methods
        self.assertEqual(str(self.classroom), "Test Class")

    def test_exercise_model(self):
        """Test Exercise Model"""
        # Fields
        self.assertEqual(self.exercise.classroom.class_name, "Test Class")
        self.assertEqual(self.exercise.exercise_name, "Test Exercise")
        self.assertEqual(self.exercise.vm_url, "test.url")
        self.assertEqual(self.exercise.description, "Test Exercise Description")
        # Methods
        self.assertEqual(str(self.exercise), "Test Exercise")

    ## URL Tests ##
    def test_url_root_redirects_to_classroomlistview(self):
        """Test url exists at correct location ClassroomListView"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)

    def test_url_exists_at_correct_location_classroomlistview(self):
        """Test url exists at correct location ClassroomListView"""
        # self.client.force_login(self.instructor)
        response = self.client.get("/classrooms/")
        self.assertEqual(response.status_code, 200)
    
    ## View Tests ##

