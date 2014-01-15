# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field skills on 'Project'
        m2m_table_name = db.shorten_name(u'portfolio_project_skills')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'portfolio.project'], null=False)),
            ('skill', models.ForeignKey(orm[u'portfolio.skill'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'skill_id'])


    def backwards(self, orm):
        # Removing M2M table for field skills on 'Project'
        db.delete_table(db.shorten_name(u'portfolio_project_skills'))


    models = {
        u'portfolio.image': {
            'Meta': {'object_name': 'Image'},
            'descripton': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['portfolio.Project']"})
        },
        u'portfolio.project': {
            'Meta': {'object_name': 'Project'},
            'cover_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descriptor': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'involvement': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['portfolio.Skill']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'portfolio.skill': {
            'Meta': {'object_name': 'Skill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['portfolio.Skill']", 'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['portfolio']