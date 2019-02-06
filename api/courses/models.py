from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    imgpath = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='course_category', null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Branch(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='branch_course', null=True)
    latitude = models.CharField(max_length=1000)
    longtitude = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)

    def __str__(self):
        return self.address


class Contact(models.Model):
    CHOISES = (
    (1, "PHONE"),
    (2, "FACEBOOK"),
    (3, "EMAIL"),
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='contact_course', null=True)
    type = models.IntegerField(choices=CHOISES, default=1)
    value = models.CharField(max_length=20)

    def __str__(self):
        return self.value
