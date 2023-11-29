from django.contrib import admin
from .models import MentorModel, AboutTeam, Courses, Contact
# Register your models here.

admin.site.register(MentorModel)
admin.site.register(AboutTeam)
admin.site.register(Courses)
admin.site.register(Contact)
