from django.shortcuts import render
from django.views import View
from .models import (
    Duties,
    Experience,
    Skill,
    Degree,
    Project,
    Certificate,
)

# Create your views here.

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

class HomeView(View):
    template_name='resume/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["experiences"] = Experience.objects.all()
        context["projects"] = Project.objects.all()
        context["skills"] = Skill.objects.all()
        context["certificates"] = Certificate.objects.all()
        context["degrees"] = Degree.objects.all()
        context["duties"] = Duties.objects.all()
        return context
    def get(self, request):
        return render(request, 'resume/home.html')

class AboutView(View):
    template_name='resume/about.html'
    def get(self, request):
        return render(request, 'resume/about.html')


class PortfolioView(View):
    template_name='resume/portfolio_item.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        p = Project.objects.filter(pk=self.kwargs.get('pk'))
        context["project_title"] = p.title
        context["description"] = p.description
        context["url"] = p.url
        return context