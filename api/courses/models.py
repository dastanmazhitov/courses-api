from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    imgpath = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    logo = models.CharField(max_length=1000)
    contacts = models.CharField(max_length=1000)
    branches = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

#
# class Branch(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     latitude = models.CharField(max_length=1000)
#     longtitude = models.CharField(max_length=1000)
#     address = models.CharField(max_length=1000)
#
#
# class Contact(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     type = models.IntegerField()
#     value = models.CharField(max_length=20)
