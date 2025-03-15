from django.db import models
from users.models import User
from django.db.models import SET_NULL


class Jobs(models.Model):
    SUSCRIPTIONS = (
        ("Free", "Free"),
        ("Paid", "Paid"),
    )
    CONTRACT_TYPES = (
        ("permanent", "Permanent"),
        ("temporary", "Temporary"),
        ("contract", "Contractor"),
        ("freelance", "Freelance"),
        ("internship", "Internship"),
        ("apprenticeship", "Apprenticeship"),
        ("fixedTerm", "Fixed-term"),
        ("seasonal", "Seasonal"),
        ("volunteer", "Volunteer"),
        ("casual", "Casual"),
    )

    SENIORITY = (
        ("trainee", "Trainee"),
        ("intern", "Intern"),
        ("junior", "Junior"),
        ("mid", "Mid-level"),
        ("senior", "Senior"),
        ("lead", "Tech Lead"),
        ("manager", "Tech Manager"),
        ("executive", "Executive"),
        ("associate", "Associate"),
        ("principal", "Principal"),
        ("vp", "Vice President"),
        ("director", "Director"),
        ("cLevel", "C-Level"),
    )
    date_posted = models.DateTimeField(null=True)
    url = models.CharField(max_length=255, unique=True)
    source = models.CharField(max_length=255, null=True, blank=True)
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()
    skills = models.JSONField(default=list, blank=True)
    contract_type = models.CharField(
        max_length=20, choices=CONTRACT_TYPES, null=True, blank=True
    )
    work_schedule = models.JSONField(default=list, blank=True)
    seniority = models.CharField(
        max_length=20, choices=SENIORITY, null=True, blank=True
    )
    subscription_type = models.CharField(
        max_length=20, choices=SUSCRIPTIONS, default="Free"
    )
    company_name = models.CharField(max_length=150, null=True, blank=True)
    job_location = models.CharField(max_length=150, null=True, blank=True)
    salary_range = models.CharField(max_length=150, null=True, blank=True)
    click_count = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    experience = models.IntegerField(null=True, default=0)
    url_direct = models.CharField(max_length=150, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=SET_NULL, null=True, blank=True, default=User)

    def __str__(self):
        return self.job_title
