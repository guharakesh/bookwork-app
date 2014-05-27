# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
import codecs

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

        with codecs.open('/home/bookwork/app/scripts/schools/out.txt', encoding='utf-8', mode='r') as f:
            data = f.readlines() 
            for line in data:
                values = line.split('|')
                sql_str = "INSERT INTO student_school VALUES (%s, '%s');" % (values[0],values[1])

                db.execute(sql_str)

        db.add_column('student_student', 'school_id', models.IntegerField(null=True))

        for stud in orm['student.Student'].objects.all():
            if stud.school == 'BOSC':
                stud.school_id = 1180
            if stud.school == 'BRAN':
                stud.school_id = 1188 
            if stud.school == 'BWRN':
                stud.school_id = 1203 
            if stud.school == 'CALT':
                stud.school_id = 1221
            if stud.school == 'CMU_':
                stud.school_id = 1262 
            if stud.school == 'CWRU':
                stud.school_id = 1267
            if stud.school == 'CW_M':
                stud.school_id = 1387
            if stud.school == 'COLU':
                stud.school_id = 1403
            if stud.school == 'CORN':
                stud.school_id = 1430
            if stud.school == 'DART':
                stud.school_id = 123 
            if stud.school == 'DUKE':
                stud.school_id = 169
            if stud.school == 'EMRY':
                stud.school_id = 215
            if stud.school == 'GRGE': 
                stud.school_id = 288
            if stud.school == 'GTCH': 
                stud.school_id = 291
            if stud.school == 'HRVD': 
                stud.school_id = 1462
            if stud.school == 'JHU_': 
                stud.school_id = 384
            if stud.school == 'LHGH': 
                stud.school_id = 424
            if stud.school == 'MIT_': 
                stud.school_id = 1583
            if stud.school == 'NYU_': 
                stud.school_id = 527 
            if stud.school == 'NRTH': 
                stud.school_id = 570
            if stud.school == 'PRIN': 
                stud.school_id = 1787
            if stud.school == 'RICE': 
                stud.school_id = 651
            if stud.school == 'STAN': 
                stud.school_id = 1997
            if stud.school == 'TUFT': 
                stud.school_id = 749
            if stud.school == 'UCLA': 
                stud.school_id = 823
            if stud.school == 'UCSD': 
                stud.school_id = 826
            if stud.school == 'UCSF': 
                stud.school_id = 827
            if stud.school == 'UCHI': 
                stud.school_id = 836
            if stud.school == 'MICH': 
                stud.school_id = 906
            if stud.school == 'UNC_': 
                stud.school_id = 941
            if stud.school == 'NRTD': 
                stud.school_id = 955
            if stud.school == 'PENN': 
                stud.school_id = 2047
            if stud.school == 'URCH': 
                stud.school_id = 2073
            if stud.school == 'USC_': 
                stud.school_id = 2084
            if stud.school == 'UVA_': 
                stud.school_id = 2132
            if stud.school == 'WISC': 
                stud.school_id = 2145
            if stud.school == 'VAND': 
                stud.school_id = 966
            if stud.school == 'WAKE': 
                stud.school_id = 990
            if stud.school == 'WUSL': 
                stud.school_id = 1012
            if stud.school == 'YALE': 
                stud.school_id = 2159
            if stud.school == 'OTHR':
                stud.school_id = 2165
            stud.save()

        db.delete_column('student_student', 'school')
        db.rename_column('student_student', 'school_id', 'school')

        # Changing field 'Student.school'
        #db.alter_column(u'student_student', 'school_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['student.School']))
        #db.execute("ALTER TABLE student_student ALTER COLUMN school_id TYPE integer USING (school_id::integer);")
        # Adding index on 'Student', fields ['school']
        db.create_index(u'student_student', ['school'])

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'student.employer': {
            'Meta': {'object_name': 'Employer'},
            'companyURL': ('django.db.models.fields.URLField', [], {'default': "'http://www.example.com'", 'max_length': '200'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'logoURL': ('django.db.models.fields.URLField', [], {'default': "'/static/img/default_employer.png'", 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'student.school': {
            'Meta': {'object_name': 'School'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'student.skill': {
            'Meta': {'object_name': 'Skill'},
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'creator'", 'null': 'True', 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skill_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['student.Student']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'student.student': {
            'Meta': {'object_name': 'Student'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile_pic': ('django.db.models.fields.files.ImageField', [], {'default': "'pic_folder/None/no-img.jpg'", 'max_length': '100'}),
            'school': ('django.db.models.fields.CharField', [], {'default': "'CWRU'", 'max_length': '50'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['student.Skill']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'year_in_school': ('django.db.models.fields.CharField', [], {'default': "'FR'", 'max_length': '2'})
        }
    }

    complete_apps = ['student']
    symmetrical = True
