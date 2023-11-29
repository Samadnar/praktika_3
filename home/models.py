from django.db import models

# Create your models here.

class MentorModel(models.Model):
    user_name = models.CharField(max_length=50)
    info_about_mentors = models.TextField()
    img = models.ImageField(upload_to='mentor/')
    profession = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.user_name
    
    
class AboutTeam(models.Model):
    motto = models.CharField(max_length=255)
    info_about_team = models.TextField()
    img = models.ImageField(upload_to='team/')
    def __str__(self) -> str:
        return self.motto

class Courses(models.Model):
    course_name = models.CharField(max_length=100)
    info_about_course = models.TextField()
    img = models.ImageField(upload_to='course/')
    price= models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self) -> str:
        return str(self.course_name) + ": $" + str(self.price)
    
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    text = models.TextField()
    def __str__(self) -> str:
        return self.name
    