# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Employer'
        db.create_table(u'employer_employer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('logoURL', self.gf('django.db.models.fields.URLField')(default='/static/img/default_employer.png', max_length=200)),
            ('companyURL', self.gf('django.db.models.fields.URLField')(default='http://www.example.com', max_length=200)),
        ))
        db.send_create_signal(u'employer', ['Employer'])


    def backwards(self, orm):
        # Deleting model 'Employer'
        db.delete_table(u'employer_employer')


    models = {
        u'employer.employer': {
            'Meta': {'object_name': 'Employer'},
            'companyURL': ('django.db.models.fields.URLField', [], {'default': "'http://www.example.com'", 'max_length': '200'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'logoURL': ('django.db.models.fields.URLField', [], {'default': "'/static/img/default_employer.png'", 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['employer']