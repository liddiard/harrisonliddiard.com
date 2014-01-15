from django.contrib import admin
from .models import Project, Image, Skill


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)} 


admin.site.register(Project, ProjectAdmin)


class ImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Image, ImageAdmin)


class SkillAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)} 


admin.site.register(Skill, SkillAdmin)
