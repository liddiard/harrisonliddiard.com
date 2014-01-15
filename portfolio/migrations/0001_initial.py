# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'portfolio_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=64)),
            ('descriptor', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('cover_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('involvement', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('summary', self.gf('django.db.models.fields.TextField')()),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('position', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'portfolio', ['Project'])

        # Adding model 'Image'
        db.create_table(u'portfolio_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('descripton', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.Project'])),
            ('position', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'portfolio', ['Image'])

        # Adding model 'Skill'
        db.create_table(u'portfolio_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=32)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.Skill'], null=True)),
        ))
        db.send_create_signal(u'portfolio', ['Skill'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'portfolio_project')

        # Deleting model 'Image'
        db.delete_table(u'portfolio_image')

        # Deleting model 'Skill'
        db.delete_table(u'portfolio_skill')


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