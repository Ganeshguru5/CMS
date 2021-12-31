from django.contrib import admin
from .models import Candidate_details,Organiser_details,Reviewer_details,selected_paper,submitted_papers
# Register your models here.

admin.site.register(Candidate_details)
admin.site.register(Organiser_details)
admin.site.register(Reviewer_details)
admin.site.register(selected_paper)
admin.site.register(submitted_papers)
