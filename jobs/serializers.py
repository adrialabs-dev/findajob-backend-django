from rest_framework import serializers
from jobs.models import Jobs
from users.serializers import UserSerializer


class JobsSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Jobs
        fields = [
            'id',
            'date_posted',
            'url',
            'source',
            'job_title',
            'job_description',
            'skills',
            'contract_type',
            'work_schedule',
            'seniority',
            'subscription_type',
            'company_name',
            'job_location',
            'salary_range',
            'click_count',
            'experience',
            'url_direct',
            'created_by',
        ]
