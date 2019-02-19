from django.test import TestCase
from .models import Course, Category

class CategoryTest(TestCase):

    def setUp(self):
        Category.objects.create(
            name='test1',
            imgpath='/test1/test1.img'
        )

        Category.objects.create(
            name='test2',
            imgpath='/test2/test2.img'
        )

    def test_category_name(self):
        category_one = Category.objects.get(name='test1')
        category_two = Category.objects.get(name='test2')

        self.assertEqual(
            category_one.name, 'test1'
        )

        self.assertEqual(
            category_two.name, 'test2'
        )


class CourseTest(TestCase):

    def setUp(self):
        cat = Category.objects.create(
            name='test',
            imgpath='/test/test.img'
        )

        Course.objects.create(
            category=cat,
            name="Test Name",
            description="Lorem Ipsum is simply dummy text.",
            logo="/test/logo.img",
        )

        Course.objects.create(
            category=cat,
            name="Test Name2",
            description="Lorem Ipsum is simply dummy text.",
            logo="/test2/logo2.img",
        )

    def test_course_name(self):
        course_one = Course.objects.get(name='Test Name')
        course_two = Course.objects.get(name='Test Name2')

        self.assertEqual(
            course_one.description, 'Lorem Ipsum is simply dummy text.'
        )

        self.assertEqual(
            course_two.logo, "/test2/logo2.img"
        )
