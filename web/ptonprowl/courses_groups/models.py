from django.db import models

# course model

class Course(models.Model):
    number = models.IntegerField(default=0, primary_key=True)
    title = models.CharField(max_length=200, unique=False)
    groups = models.TextField()

    def __str__(self):
        return str(self.number) + ": " + self.title



class CourseID(models.Model):
    id = models.CharField(max_length=255, unique=True, primary_key=True)
    # unique??!
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.id + " - " + self.course.__str__()

class Group(models.Model):
    members = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
