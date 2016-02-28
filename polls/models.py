import datetime
from django.db import models
from django.utils import timezone



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class Report(models.Model):
    subject = models.CharField(max_length=200)
    timestamp = models.DateTimeField(default=timezone.now)
    long_text = models.TextField(max_length=1000)
    short_text = models.CharField(max_length=200)
    user_id = models.IntegerField(default=0)
    private = models.BooleanField(default=False)
    file = models.FileField(upload_to='./upload/')
    folder_id = models.IntegerField(default=777)
    location = models.CharField(max_length=200, default='NA')
    kw = models.CharField(max_length=200, default='')
    file2 = models.FileField(upload_to='./upload/',blank=True)
    datetime = models.CharField(max_length=200, default='YYYY-MM-DD')
    #datetime = models.DateField(blank=True, default=datetime.now().strftime("%d.%m.%Y"))



    
    def __str__(self):
        return self.subject



class Folder(models.Model):
    name = models.CharField(max_length=200)
    owner_id = models.IntegerField(default=0)

    def __str__(self):
        return self.name




