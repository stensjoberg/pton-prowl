from django.db import models

# course model

class Course(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    title = models.CharField(max_length=200, unique=False)
    groups = models.TextField()

    def __str__(self):
        return str(self.id) + ": " + self.title

class Code(models.Model):
    code = models.CharField(max_length=255, unique=True, primary_key=True)
    # unique??!
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.code + " - " + self.course.__str__()

class Group(models.Model):
    members = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
