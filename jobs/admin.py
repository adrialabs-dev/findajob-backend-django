from django.contrib import admin
from jobs.models import Jobs

@admin.register(Jobs)
class PostAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'created_by', 'created_at')
    list_filter = ('date_posted','created_by', 'created_at')
    search_fields = ('job_title', 'job_description')