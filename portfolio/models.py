from django.db import models

MEDIA_BASE = 'portfolio/img/'

class Project(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    descriptor = models.CharField(max_length=128)
    cover_image = models.ImageField(upload_to=MEDIA_BASE+'covers')
    involvement = models.CharField(max_length=32)
    skills = models.ManyToManyField('Skill')
    link = models.URLField(blank=True)
    github = models.URLField(blank=True)
    summary = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    position = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to=MEDIA_BASE+'projects')
    descripton = models.TextField(blank=True)
    project = models.ForeignKey('Project')
    position = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return "(%s) %s" % (self.project, self.description)


class Skill(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    parent = models.ForeignKey('self', null=True, blank=True)

    def __unicode__(self):
        return self.name
