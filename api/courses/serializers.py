from rest_framework import serializers
from .models import *



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ('id', )


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        exclude = ('id', 'course')



class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        exclude = ('id', 'course')


class CourseSerializer(serializers.ModelSerializer):
    branches = BranchSerializer(many=True)
    contacts = ContactSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'category', 'logo', 'contacts', 'branches')
