import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
     # ...
    def __str__(self):
        return self.question_text

    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # ...
    def __str__(self):
        return self.choice_text

class InfoModelForm(models.Model):
    name = models.CharField('名前',max_length=255)
    mail = models.EmailField('メール',max_length=255)
    gender = models.BooleanField('性別')
    department = models.CharField('部署',max_length=255)
    year = models.IntegerField('社歴',default=0)
    created_at = models.DateField('作成日',default=timezone.now)

    def __str__(self):
        return '<id:' + str(self.id) + ',' + self.name + ',' + self.department + '>'

# Create your models here.
