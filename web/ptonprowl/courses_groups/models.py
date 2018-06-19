from django.db import models

# course model

class Course(models.Model):
    def __init__(self, name, course_id, groups):
        self.name = name
        self.course_id = course_id
        self.groups = groups
