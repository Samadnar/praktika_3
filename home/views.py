from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DetailView , UpdateView
from django.shortcuts import render
from .models import MentorModel, AboutTeam, Courses, Contact
from .forms import ContactForm


# Create your views here.



def mentorview(request):
    mentor = MentorModel.objects.all()
    context = {
        'mentor' : mentor
    }
    
    return render(request, 'trainers.html', context)

def indexview(request):
    mentor = MentorModel.objects.all()
    about_team = AboutTeam.objects.all().last()
    courses = Courses.objects.all()
    context = {
        'mentor_for_index' : mentor,
        'about_team_index' : about_team,
        'courses_index' : courses
    }
    
    return render(request, 'index.html', context)


def aboutview(request):
    about_team = AboutTeam.objects.all().last()
    context = {
        'about' : about_team
    }
    return render(request, 'about.html', context)

def coursesview(request):
    courses = Courses.objects.all()
    context = {
        'courses' : courses
    }
    return render(request, 'courses.html', context)

def contactview(request):
    contactform = ContactForm(request.POST)
    if request.POST and contactform.is_valid:
        contactform.save()
    return render(request, 'contact.html', {})