from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class CourseList(APIView):

    def get(self, request):
        category = Category.objects.all()
        course = Course.objects.all()
        branch = Course.objects.all()
        contact = Contact.objects.all()
        category_serializer = CategorySerializer(category, many=True)
        course_serializer = CourseSerializer(course, many=True)
        contact_serializer = ContactSerializer(contact, many=True)
        branch_serializer = BranchSerializer(branch, many=True)

        response = category_serializer.data + branch_serializer.data + contact_serializer.data + branch_serializer.data

        return Response(response)

    def post(self):
        pass
