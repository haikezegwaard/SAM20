from django.contrib import admin
from monitor.models import Project, Summary, InterestProject

# Register your models here.
admin.site.register(Project)
admin.site.register(Summary)
admin.site.register(InterestProject)
