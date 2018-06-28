from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, netid, password=None):
        """
        Creates and saves a User with the given netid, email and password.
        """
        if not (netid or email or full_name or class_year):
            raise ValueError('Users must have all the things')

        user = self.model(
            netid=netid,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, netid, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            netid,
            password=password,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    # unique identifier NETID
    netid = models.CharField(max_length=40,
                             unique=True,
                             verbose_name="NetID",
                             help_text="Use your Princeton-issued netID."
                             )

    # full name
    full_name = models.CharField(max_length=40,
                                 unique=False,
                                 verbose_name="Full name",
                                 help_text="Your full name."
                                 )

    # while a number, a class year makes more sense to store as chars
    class_year = models.CharField(max_length=4,
                                 verbose_name="Class Year",
                                 help_text="Your class year, <em>YYYY</em>"
                                 )

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'netid'

    # required field upon account creation
    REQUIRED_FIELDS = []

    class Meta:
        indexes = [models.Index(fields=['full_name'])]
        ordering = ['-full_name']
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.netid

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
        return self.is_superuser
