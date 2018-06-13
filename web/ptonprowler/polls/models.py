import datetime

from django.db import models
<<<<<<< Updated upstream
from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # to string method
    def __str__(self):
        return self.question_text
    # custom method
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


=======
from django.utils import timezone

# Create your models here.

# questions class
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


    def was_published_recently(self):
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

# choices class
>>>>>>> Stashed changes
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
<<<<<<< Updated upstream
    # to string method
    def __str__(self):
        return self.choice_text
=======

    def __str__(self):
            return self.choice_text
>>>>>>> Stashed changes
