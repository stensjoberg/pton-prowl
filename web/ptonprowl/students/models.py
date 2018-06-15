from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class StudentManager(BaseUserManager):
    def create_user(self, netid, email, full_name, class_year, password=None):
        """
        Creates and saves a User with the given netid, email and password.
        """
        if not (netid or email or full_name or class_year):
            raise ValueError('Users must have all the things')

        user = self.model(
            netid=netid,
            email=self.normalize_email(email),
            full_name=full_name,
            class_year=class_year,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, netid, email, full_name, class_year, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            netid,
            email,
            full_name,
            class_year,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Student(AbstractBaseUser):

    # unique identifier NETID
    netid = models.CharField(max_length=40,
                             unique=True,
                             help_text="Use your Princeton-issued netID.")

    # email is the unique identifier plus '@princeton.edu'
    # redundant redundant?
    # TODO: Implement setter/getter to connect netid and email
    email = models.EmailField(max_length=255,
                             unique=True,
                             help_text="Please use Princeton email.")

    # full name
    full_name = models.CharField(max_length=40,
                                 help_text="Your full name.")

    # while a number, a class year makes more sense to store as chars
    class_year = models.CharField(max_length=4,
                                 help_text="Your class year, <em>YYYY</em>")


    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = StudentManager()

    # AbstractBaseUser requires unique identifier if using standard backend
    # TODO: switch to non-standard pton CAS backend (ask michael?)
    USERNAME_FIELD = 'netid'
    EMAIL_FIELD = 'email'

    # required field upon account creation
    REQUIRED_FIELDS = [ 'email', 'full_name', 'class_year']

    def __str__(self):
        return self.email + " | " + self.full_name + " " + self.class_year

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
