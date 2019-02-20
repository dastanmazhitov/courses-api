from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
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


class CoursePostTest(APITestCase):

    print(Category.objects.all())
    def test_create_course(self):
        url = reverse('courses')
        data = {
                  "name": "English Zone",
                  "description": "Миссия English Zone заключается в том, чтобы помочь людям раскрыть весь их потенциал.",
                  "category": 8,
                  "logo": "http://www.answersfrom.com/wp-content/uploads/2011/09/Not-talanted-but-curious.jpg",
                  "contacts": [
                    {
                      "type": 1,
                      "value": "0770 792 299"
                    },
                    {
                      "type": 2,
                      "value": "https://www.facebook.com/english.zone.kg/"
                    },
                    {
                      "type": 3,
                      "value": "ezone.kg@gmail.com"
                    }
                  ],
                  "branches": [
                    {
                      "address": "Manas 58/ Aini - right next to the Manas university",
                      "latitude": "42.847971",
                      "longitude": "74.586733"
                    },
                    {
                      "address": "Бишкек, Юг-2 дом 15а Советская/Горького",
                      "latitude": "42.8586017",
                      "longitude": "74.6068425"
                    }
                  ]
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 1)
        self.assertEqual(Course.objects.get().name, 'English Zone')
