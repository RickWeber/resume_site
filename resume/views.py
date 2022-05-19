from django.shortcuts import render
from django.views.generic import TemplateView
from .models import (
    Duties,
    Experience,
    ProfessionalSummary,
    Skill,
    Degree,
    Project,
    Certificate,
    Blurb
)

def home(request):
    context = {
        'experiences': Experience.objects.all(),
        'projects': Project.objects.all(),
        'skills': Skill.objects.all(),
        'certificates': Certificate.objects.all(),
        'degrees': Degree.objects.all(),
        'duties': Duties.objects.all()
    }
    for ex in context['experiences']:
        duties = Duties.objects.filter(pk=context['experiences'][ex])
        context['experiences'][ex]['duties'] = duties
    return render(request, 'resume/home.html', context)

class HomeView(TemplateView):
    template_name='resume/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["experiences"] = Experience.objects.all()
        context["projects"] = Project.objects.all()
        context["skills"] = Skill.objects.all()
        context["certificates"] = Certificate.objects.all()
        context["degrees"] = Degree.objects.all()
        context["duties"] = Duties.objects.all()
        context["blurb"] = Blurb.objects.last()
        context["summary"] = ProfessionalSummary.objects.last()
        return context

class AboutView(TemplateView):
    template_name='resume/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blurb"] = Blurb.objects.last()
        context["summary"] = ProfessionalSummary.objects.last()
        return context


class PortfolioView(TemplateView):
    template_name='resume/portfolio_item.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        p = Project.objects.filter(pk=self.kwargs.get('pk'))
        context["project_title"] = p.title
        context["description"] = p.description
        context["url"] = p.url
        return context
