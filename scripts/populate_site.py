import json
from resume.models import (
    Organization,
    Skill,
    Certificate,
    Degree,
    Duties,
    ProfessionalSummary,
    Project,
    Experience
)

clear_class = lambda c: c.objects.all().delete()

def run():
    """import resume details and 
    load them into the appropriate 
    objects."""
    with open('resume.json') as json_file:
        data = json.load(json_file)

    for model_type in data.keys():
        for x in data[model_type]:
            thing = eval(model_type).objects.get_or_create(data[model_type][x])
            thing.save()

#if __name__ == '__main__':
#    run()