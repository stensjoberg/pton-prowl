from django.db import models

from users.models import User

#
# A Princeton course model includes unique id, codes, title and users
#
class Course(models.Model):

    # unique course number and pk
    id = models.IntegerField(default=0, primary_key=True)

    # verbose title of course
    title = models.CharField(max_length=200, unique=False)

    # there are many users in one course and one user can be in
    # many courses
    users = models.ManyToManyField(User)

    # adds user to course
    def add_user(self, user):
        self.users.add(user)
        self.save()
        return self.users.get(netid=user.netid)

    # remove user from course
    def remove_user(self, user):
        user = self.users.get(netid=user.netid)
        self.user.remove(user)
        self.save()
        return user

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
# A study group has an associated course and member users
#
class Group(models.Model):

    # each course has many groups
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='groups')

    # each user can be in many groups
    users = models.ManyToManyField(User)

    # sets this group's course
    def set_course(self, course):
        self.course = course
        self.save()
        return self.course

    # adds a user to the course through fk relationship
    def add_user(self, user):

        #if user.course_set.get(id=self.course.id) is None:
        #    raise ValueError("User not in group's course")

        self.users.add(user)
        self.save()
        return self.users.get(netid=user.netid)

    # remove user from group
    def remove_user(self, user):
        user = self.users.get(netid=user.netid)
        self.user.remove(user)
        self.save()
        return user

    def __str__(self):
        return self.course.__str__() + " (" + str(self.id) + ")"
