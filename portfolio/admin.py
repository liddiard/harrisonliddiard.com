from django.contrib import admin
from .models import Project, Image, Skill


class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)


class ImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Image, ImageAdmin)


class SkillAdmin(admin.ModelAdmin):
    pass

admin.site.register(Skill, SkillAdmin)
