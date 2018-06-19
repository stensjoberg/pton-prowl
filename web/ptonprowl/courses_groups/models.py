from django.db import models

# course model

class Course(models.Model):
    number = models.CharField(max_length = 6, unique = True)
    # courseid = models.CharField(max_length=6, unique=True)
    name = models.CharField(max_length=200, unique=True)
    groups = models.TextField()

class CourseID(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Group(models.Model):
    groupid =  models.CharField(max_length=3, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    members = models.TextField()
