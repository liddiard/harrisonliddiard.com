from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404

from .models import Project, Skill, Image


class FrontView(TemplateView):

    template_name = "portfolio_front.html"
    
    def get_context_data(self, **kwargs):
        context = super(FrontView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.order_by('position')
        return context


class ProjectView(TemplateView):

    template_name = "project.html"

    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        project_slug = self.kwargs.get('project')
        project = get_object_or_404(Project, slug=project_slug)
        gallery = Image.objects.filter(project=project).order_by('position')
        context['project'] = project
        context['skills'] = project.skills.all()
        context['gallery'] = gallery
        return context


class SkillView(TemplateView):

    template_name = "skill.html"

    def get_context_data(self, **kwargs):
        context = super(SkillView, self).get_context_data(**kwargs)
        skill_slug = self.kwargs.get('skill')
        skill = get_object_or_404(Skill, slug=skill_slug)
        projects = Project.objects.filter(skills=skill)
        context['skill'] = skill
        context['projects'] = projects
        return context


class ResumeView(TemplateView):
    
    template_name = "resume.html"
