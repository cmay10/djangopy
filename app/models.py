from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=5)

class GoverningBody(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=5)
    state = models.ForeignKey(State,on_delete=models.CASCADE)

class PlayoffRound(models.Model):
    name = models.CharField(max_length=50)
    number = models.PostiveSmallIntegerField()
    governing_body = models.ForeignKey(GoverningBody)

class Alignment(models.Model):
    name = models.CharField(max_length=50)
    governing_body = models.ForeignKey(GoverningBody)

class Season(models.Model):
    year = models.PostiveSmallIntegerField()
    alignment = models.ForeignKey(Alignment,on_delete=models.CASCADE)

class Week(models.Model):
    number = models.PostiveSmallIntegerField()
    description = models.CharField(max_length=50)
    season = models.ForeignKey(Season,on_delete=models.CASCADE)

class Conference(models.Model):
    classification = models.CharField(max_length=5)
    division = models.PostiveSmallIntegerField()
    season = models.ForeignKey(Season,on_delete=models.CASCADE)

class Region(models.Model):
    number = models.PostiveSmallIntegerField()
    classification = models.ForeignKey(Conference,on_delete=models.CASCADE)

class District(models.Model):
    number = models.PostiveSmallIntegerField()
    Region = models.ForeignKey(Region,on_delete=models.CASCADE)

class Color(models.Model):
    name = models.CharField(max_length=20)
    r = models.PostiveSmallIntegerField()
    g = models.PostiveSmallIntegerField()
    b = models.PostiveSmallIntegerField()
    hex_code = models.Charfield(max_length=10)

class Stadium(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)

class School(models.Model):
    name = models.CharField(max_length=100)
    mascot = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    home_stadium = models.ForeignKey(Stadium,on_delete=models.CASCADE)
    primary_color = models.ForeignKey(Color,on_delete=models.CASCADE)
    secondary_colors = models.ManyToManyField(Color)

class Team(models.Model):
    school = models.OneToOneField(school)
    district = models.ForeignKey()

class Game(models.Model):
    away_team = models.ForeignKey(Team,on_delete=models.CASCADE)
    home_team = models.ForeignKey(Team,on_delete=models.CASCADE)
    stadium = models.ForeignKey(Stadium,on_delete=models.CASCADE)
    date = models.DateTimeField()
    week = models.ForeignKey(Week,on_delete=models.CASCADE)

class Score(models.Model):
    away_score = PostiveSmallIntegerField()
    home_score = PostiveSmallIntegerField()
    quarter = PostiveSmallIntegerField()
    minutes = PostiveSmallIntegerField()
    seconds = PostiveSmallIntegerField()
    poster = models.ForeignKey(User)

class Thread(models.Model):
    name = models.CharField(max_length=200)
    game = models.ForeignKey(Game,on_delete=models.CASCADE)

class Post(models.Model):
    thread = models.ForeignKey(Thread)
    author = models.ForeignKey(User)



    






