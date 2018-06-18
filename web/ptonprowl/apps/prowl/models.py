from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    course_id = models.CharField(max_length=6, unique=True)
    # array of group_ids from the group model
    groups = []

class Group(models.Model):
    group_id = models.CharField(max_length=3, unique=True)
    course = models.CharField(max_length=6, unique=True)
    # array of net_ids from the student model
    members = []
