from django.db import models
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
from students.models import Student

#
# A Princeton course model includes unique id, codes, title and students
#
class Course(models.Model):

    # unique course number and pk
    id = models.IntegerField(default=0, primary_key=True)

    # verbose title of course
    title = models.CharField(max_length=200, unique=False)
<<<<<<< Updated upstream
=======
    groups = models.ManyToManyField(Group)
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
#
# A Princeton course code like 'COS216', has the code itself and its course
#
=======
    # def addgroup(self, group):

>>>>>>> Stashed changes
class Code(models.Model):

    # the code (and pk)
    code = models.CharField(max_length=255, unique=True, primary_key=True)
<<<<<<< Updated upstream

    # each course has many codes
=======
>>>>>>> Stashed changes
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.code

#
# A study group has an associated course and member students
#
class Group(models.Model):
<<<<<<< Updated upstream

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
=======
    members = models.ManyToManyField(Student)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    time = models.TextField()

    def __str__(self):
        return self.id + " - " + Truncator(self.members).words(5) + "..."
"""
    def add_member(self, student):


    def remove_member(self, student):
"""
>>>>>>> Stashed changes
