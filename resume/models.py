from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    industry = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.name


class Experience(models.Model):
    title = models.CharField(max_length=50)
    #location = models.CharField(max_length=100) # TODO: I can drop this
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    start = models.CharField(max_length=35)
    end = models.CharField(max_length=35)
    def __str__(self):
        return self.title


class Duties(models.Model):
    class Meta:
        verbose_name = "Duty"
        verbose_name_plural = "Duties"
    short_description = models.CharField(max_length=50, default="duty description")
    description = models.CharField(max_length=250)
    #job = models.ForeignKey(Experience, on_delete=models.CASCADE)
    job = models.ManyToManyField(Experience)
    order = models.IntegerField()
    def __str__(self):
        return self.short_description


class Degree(models.Model):
    name = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    school = models.ForeignKey(Organization, on_delete=models.CASCADE)
    year = models.DateField()
    distinctions = models.CharField(max_length=30, null=True, blank=True)
    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True, blank=True)
    issuer = models.CharField(max_length=50)
    date = models.DateField()
    url = models.URLField()
    def __str__(self):
        return self.name


class Skill(models.Model):
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        ordering = ["level"]
    name = models.CharField(max_length=40, blank=True, null=True)
    comments = models.CharField(max_length=100, null=True, blank=True)
    LEVELS = (
        ('a','Advanced'),
        ('b','Intermediate'),
        ('c','Novice'),
    )
    level = models.CharField(max_length=20, choices=LEVELS)
    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500, null=True, blank=True)
    url = models.URLField()
    def __str__(self):
        return self.title


class ProfessionalSummary(models.Model):
    elevator_pitch = models.CharField(max_length=250, null=True, blank=True)
    tech_skills = models.CharField(max_length=250, null=True, blank=True)
    soft_skills = models.CharField(max_length=250, null=True, blank=True)
    def __str__(self):
        return f"Summary #{self.pk}"


class Blurb(models.Model):
    blurb = models.TextField()
    def __str__(self):
        return self.blurb[:50] if len(self.blurb) > 50 else self.blurb

#class UserProfile(models.Model):
#    pass
#class ContactProfile(models.Model):
#    pass
#class Media(models.Model):
#    image = models.ImageField(blank=True, null=True) # Do I need "upload_to" field?
#    url = models.URLField(blank=True, null=True)
#    name = models.CharField(max_length=200)
#    def save(self, *args, **kwargs):
#        if self.url: