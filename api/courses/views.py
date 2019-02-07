from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class CourseList(APIView):

    def get(self, request):
        course = Course.objects.all()
        course_serializer = CourseSerializer(course, many=True)
        return Response(course_serializer.data)

    def post(self, request, format=None):
        serializer = CourseSerializer(request.data)
        if serializer.is_valid():
            instance = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseById(APIView):

    def get(self, request, course_id):
        course = Course.objects.filter(pk=course_id)
        course_serializer = CourseSerializer(course, many=True)
        return Response(course_serializer.data)


    def delete(self, request, course_id):
        Course.objects.filter(pk=course_id).delete()
        return Response(serializer.data, status=status.HTTP_2HTTP_200_OK)
