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
            crn = "129999999999",
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
        self.assertEqual(self.classroom.crn, "129999999999")
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
        response = self.client.get("/classrooms/")
        self.assertEqual(response.status_code, 200)

    ## View Tests ##
    def test_classroom_list_view(self):
        """Test Classroom ListView"""
        self.client.force_login(self.instructor)
        response = self.client.get(reverse("classroom_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.instructor.email)
        self.assertContains(response, "Test Class")
        self.assertContains(response, "instructor@fakeemail.com")
        self.assertContains(response, "129999999999")
        self.assertContains(response, "* / 30")

    def test_classroom_detail_exercise_list_view(self):
        """Test Classroom Detail / Exercise List View"""
        self.client.force_login(self.instructor)
        response = self.client.get(reverse("classroom_detail_exercise_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Classroom")
        self.assertContains(response, self.instructor.email)
        self.assertContains(response, "129999999999")
        self.assertContains(response, "Test Exercise")
        self.assertContains(response, "Test Exercise Description")
        self.assertContains(response, "Due Date: ")
        self.assertContains(response, "* %")
