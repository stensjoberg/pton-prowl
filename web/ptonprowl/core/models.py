from django.db import models

from students.models import Student

#
# A Princeton course model includes unique id, codes, title and students
#
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

    # remove student from course
    def remove_student(self, student):
        student = self.students.get(netid=student.netid)
        self.student.remove(student)
        self.save()
        return student

    # returns string representation
    def __str__(self):
        return self.title + " (" + str(self.id) + ")"

#
# A Princeton course code like 'COS216', has the code itself and its course
#
class Code(models.Model):

    # the code (and pk)
    code = models.CharField(max_length=255, unique=True, primary_key=True)

    # each course has many codes
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.code

#
# A study group has an associated course and member students
#
class Group(models.Model):

    # each course has many groups
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    # each student can be in many groups
    students = models.ManyToManyField(Student)

    # sets this group's course
    def set_course(self, course):
        self.course = course
        self.save()
        return self.course

    # adds a student to the course through fk relationship
    def add_student(self, student):

        #if student.course_set.get(id=self.course.id) is None:
        #    raise ValueError("Student not in group's course")

        self.students.add(student)
        self.save()
        return self.students.get(netid=student.netid)

    # remove student from group
    def remove_student(self, student):
        student = self.students.get(netid=student.netid)
        self.student.remove(student)
        self.save()
        return student

    def __str__(self):
        return self.course.__str__() + " (" + str(self.id) + ")"
