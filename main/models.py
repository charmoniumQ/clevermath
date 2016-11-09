from django.db import models

# Create your models here.
class Problem(models.Model):
    title = models.CharField(max_length=127)
    description = models.TextField()
    solution = models.TextField()
    answer = models.IntegerField()
    answer_prog = models.TextField()

class User(models.Model):
    username = models.CharField(max_length=127)
    email = models.CharField(max_length=127)
    firstname = models.CharField(max_length=127)
    lastname = models.CharField(max_length=127)
    levels = models.IntegerField()
    points = models.IntegerField()

class UserProblem(models.Model):
    user = models.ForeignKey(User)
    problem = models.ForeignKey(Problem)
    # comma separated string with previous guesses
    previous = models.CharField(max_length=127)
    # number of guesses, negative if correct
    guesses = models.IntegerField()
