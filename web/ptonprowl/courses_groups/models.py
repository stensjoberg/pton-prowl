from django.db import models

# course model

class Course(models.Model):
    number = models.IntegerField(default=0, primary_key=True)
    title = models.CharField(max_length=200, unique=False)
    groups = models.TextField()

class CourseID(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Group(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    members = models.TextField()
