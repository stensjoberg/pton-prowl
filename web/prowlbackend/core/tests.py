from django.test import TestCase

from core.models import Course, Group, Code
from users.models import User

# models tests
class CourseTest(TestCase):

    def setUp(self):
        Course.objects.create(id=12345,title="Test Title")
        User.objects.create(netid='test', full_name="Test Testson", class_year="2021")

    def test_course_string(self):
        course = Course.objects.get(id=12345)
        self.assertEqual(course.__str__(), "Test Title (12345)")

    def test_user_addition(self):
        course = Course.objects.get(id=12345)
        user = User.objects.get(netid='test')
        res = course.add_user(user)
        self.assertEqual(res, user)

    def test_user_deletion(self):
        course = Course.objects.get(id=12345)
        user = User.objects.get(netid='test')
        course.add_user(user)
        res = course.remove_user(user)
        with self.assertRaises(User.DoesNotExist):
            query = course.users.get(netid=user.netid)
        self.assertEqual(res, user)

class GroupTest(TestCase):

    def setUp(self):
        Course.objects.create(id=12345,title="Test Title")
        Group.objects.create(id=1, course=Course.objects.get(id=12345))
        User.objects.create(netid='test', full_name="Test Testson", class_year="2021")

    def test_course_string(self):
        group = Group.objects.get(id=1)
        self.assertEqual(group.__str__(), "1 (12345)")

    def test_valid_user_addition(self):
        course = Course.objects.get(id=12345)
        user = User.objects.get(netid='test')
        group = Group.objects.get(id=1)
        course.add_user(user)
        res = group.add_user(user)
        self.assertEqual(res, user)

    def test_invalid_user_addition(self):
        course = Course.objects.get(id=12345)
        user = User.objects.get(netid='test')
        group = Group.objects.get(id=1)
        with self.assertRaises(Course.DoesNotExist):
            res = group.add_user(user)

    def test_user_deletion(self):
        course = Course.objects.get(id=12345)
        user = User.objects.get(netid='test')
        group = Group.objects.get(id=1)
        course.add_user(user)
        res = course.remove_user(user)
        with self.assertRaises(User.DoesNotExist):
            query = course.users.get(netid=user.netid)
        self.assertEqual(res, user)
