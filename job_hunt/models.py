from django.db import models

# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(null=True, blank=True)


class Position(models.Model):
    title = models.CharField(max_length=50)
    listing = models.TextField(null=True, blank=True) # copy the html of the listing page
    url = models.URLField(null=True, blank=True)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)


class Application(models.Model):
    to_specific_listing = models.BooleanField()
    listing = models.ForeignKey(Position, on_delete=models.DO_NOTHING)
    url = models.URLField(null=True, blank=True)
    contact_person = models.EmailField()
    notes = models.TextField()

class Coverletter(models.Model):
    file = models.FilePathField()
    application = models.ForeignKey(Application, on_delete=models.DO_NOTHING)