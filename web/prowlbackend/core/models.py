from django.db import models

from users.models import User

"""
    A Princeton course model includes unique id, codes, title and users
"""
class Course(models.Model):

    # unique course number and pk
    id = models.IntegerField(default=0,
                             primary_key=True,
                             help_text="The registrar's unique ID."
                             )

    # verbose title of course
    title = models.CharField(max_length=200,
                             unique=False,
                             help_text="Full course title."
                             )

    # there are many users in one course and one user can be in
    # many courses
    users = models.ManyToManyField(User,
                                  related_name='courses',
                                  related_query_name='course')

    class Meta:
        verbose_name = "course"
        verbose_name_plural = "courses"

    # returns string representation
    def __str__(self):
        return "%s (%s)" % (self.title, self.id)

    # adds user to course
    def add_user(self, user):
        self.users.add(user)
        self.save()
        return self.users.get(netid=user.netid)

    # remove user from course
    def remove_user(self, user):
        user = self.users.get(netid=user.netid)
        self.users.remove(user)
        self.save()
        return user

"""
    A Princeton course code like 'COS216', has the code itself and its course
"""
class Code(models.Model):

    # the code (and pk)
    id = models.CharField(max_length=255,
                            unique=True,
                            primary_key=True
                            )

    # each course has many codes
    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               related_name='codes',
                               related_query_name='code'
                               )

    class Meta:
        verbose_name = "course code"
        verbose_name_plural = "course codes"

    def __str__(self):
        return "%s (%s)" % (self.id, self.course.id)

#
# A study group has an associated course and member users
#
class Group(models.Model):

    # each course has many groups
    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               related_name='groups',
                               related_query_name='group'
                               )

    # each user can be in many groups
    users = models.ManyToManyField(User,
                                   related_name='groups',
                                   related_query_name='group')

    def __str__(self):
        return "%s (%s)" % (self.id, self.course.id)

    # sets this group's course
    def set_course(self, course):
        self.course = course
        self.save()
        return self.course

    # adds a user to the course through fk relationship
    def add_user(self, user):

        # this raises DoesNotExist error if user trying to join
        # is not in course intentionally
        user.courses.get(id=self.course.id)

        self.users.add(user)
        self.save()
        return self.users.get(netid=user.netid)

    # remove user from group
    def remove_user(self, user):
        user = self.users.get(netid=user.netid)
        self.user.remove(user)
        self.save()
        return user
