from django import template
from resume.models import Duties

register = template.Library()

@register.filter
def duties_by_job(job):
    return Duties.objects.filter(job__experience=job)

@register.filter
def is_this_job(duties, job):
    return Duties.objects.filter(job__experience=job)