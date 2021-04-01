from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=20)
    dp = models.ImageField(upload_to='pics')
    birth = models.DateField()
    phone = models.PositiveBigIntegerField()
    email = models.EmailField()
    add = models.CharField(max_length=100)
    descp = models.TextField()
    hobbies = models.TextField()

class Skills(models.Model):
    skill_name = models.CharField(max_length=50)
    skill_rate = models.IntegerField()

class Education(models.Model):
    quali = models.CharField(max_length=30)
    special = models.CharField(max_length=30)
    insti = models.CharField(max_length=50)
    year = models.IntegerField()
    board = models.CharField(max_length=30)
    grades = models.FloatField()

class Projects(models.Model):
    proj_name = models.CharField(max_length=100)
    proj_descp = models.TextField()
    proj_url = models.URLField()

class Experience(models.Model):
    job_name = models.CharField(max_length=80)
    job_comp = models.CharField(max_length=100)
    job_descp = models.IntegerField()
    job_year = models.DateField

class Extra_Curri(models.Model):
    curri_year = models.IntegerField()
    curri_desc = models.TextField()

class Language(models.Model):
    lang = models.CharField(max_length=100)