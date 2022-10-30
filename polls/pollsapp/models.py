from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200)
    date = models.DateTimeField('date published')

    def __str__(self):
        return f"{self.question}"


class Choice(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.choice}. Votes: {self.votes}"