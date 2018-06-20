from django.db import models

from students.models import Student

# course model

class Course(models.Model):

    # unique course number and pk
    id = models.IntegerField(default=0, primary_key=True)

    # verbose title of course
    title = models.CharField(max_length=200, unique=False)

    # there are many students in one course and one student can be in
    # many courses
    students = models.ManyToManyField(Student)

    # adds student to course
    def add_student(self, student):
        self.students.add(student)
        self.save()
        return self.students.get(netid=student.netid)

    # returns string representation
    def __str__(self):
        return str(self.id) + ": " + self.title

class Code(models.Model):

    # the code (and pk)
    code = models.CharField(max_length=255, unique=True, primary_key=True)

    # each course has many codes
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.code + " - " + self.course.__str__()

class Group(models.Model):

    # each course has many groups
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    # each student can be in many groups
    students = models.ManyToManyField(Student)

    # sets this group's course
    def set_course(self, course):
        self.course = course
        return self.course

    def add_student(self, student):

        if student.course_set.get(id=self.course.id) is None:
            raise ValueError("Student not in group's course")

        self.students.add(student)
        self.save()
        return self.students.get(netid=student.netid)
