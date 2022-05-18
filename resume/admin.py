from django.contrib import admin
from .models import (
    Organization,
    Experience,
    Duties,
    Degree,
    Certificate,
    Skill,
    Project,
    ProfessionalSummary
)

admin.site.register(Organization)
admin.site.register(Experience)
admin.site.register(Duties)
admin.site.register(Degree)
admin.site.register(Certificate)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(ProfessionalSummary)