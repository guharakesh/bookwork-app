# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
import codecs


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'School'
        db.create_table(u'student_school', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'student', ['School'])

        with codecs.open('/home/bookwork/app/scripts/schools/out.txt', encoding='utf-8', mode='r') as f:
            data = f.readlines() 
            for line in data:
                values = line.split('|')
                sql_str = "INSERT INTO student_school VALUES (%s, '%s');" % (values[0],values[1])
                #db.execute("INSERT INTO student_school VALUES ({0}, '{1}');".format(values[0],values[1]))

                db.execute(sql_str)


        # Renaming column for 'Student.school' to match new field type.
        db.rename_column(u'student_student', 'school', 'school_id')

        for student in orm['student.Student'].objects.all():
            if student.school == 'BOSC':
                student.school = 1180
            if student.school == 'BRAN':
                student.school = 1188 
            if student.school == 'BWRN':
                student.school = 1203 
            if student.school == 'CALT':
                student.school = 1221
            if student.school == 'CMU_':
                student.school = 1262 
            if student.school == 'CWRU':
                student.school = 1267
            if student.school == 'CW_M':
                student.school = 1387
            if student.school == 'COLU':
                student.school = 1403
            if student.school == 'CORN':
                student.school = 1430
            if student.school == 'DART':
                student.school = 123 
            if student.school == 'DUKE':
                student.school = 169
            if student.school == 'EMRY':
                student.school = 215
            if student.school == 'GRGE': 
                student.school = 288
            if student.school == 'GTCH': 
                student.school = 291
            if student.school == 'HRVD': 
                student.school = 1462
            if student.school == 'JHU_': 
                student.school = 384
            if student.school == 'LHGH': 
                student.school = 424
            if student.school == 'MIT_': 
                student.school = 1583
            if student.school == 'NYU_': 
                student.school = 527 
            if student.school == 'NRTH': 
                student.school = 570
            if student.school == 'PRIN': 
                student.school = 1787
            if student.school == 'RICE': 
                student.school = 651
            if student.school == 'STAN': 
                student.school = 1997
            if student.school == 'TUFT': 
                student.school = 749
            if student.school == 'UCLA': 
                student.school = 823
            if student.school == 'UCSD': 
                student.school = 826
            if student.school == 'UCSF': 
                student.school = 827
            if student.school == 'UCHI': 
                student.school = 836
            if student.school == 'MICH': 
                student.school = 906
            if student.school == 'UNC_': 
                student.school = 941
            if student.school == 'NRTD': 
                student.school = 955
            if student.school == 'PENN': 
                student.school = 2047
            if student.school == 'URCH': 
                student.school = 2073
            if student.school == 'USC_': 
                student.school = 2084
            if student.school == 'UVA_': 
                student.school = 2132
            if student.school == 'WISC': 
                student.school = 2145
            if student.school == 'VAND': 
                student.school = 966
            if student.school == 'WAKE': 
                student.school = 990
            if student.school == 'WUSL': 
                student.school = 1012
            if student.school == 'YALE': 
                student.school = 2159
            if student.school == 'OTHR':
                student.school = 2165

            student.save()

        # Changing field 'Student.school'
        #db.alter_column(u'student_student', 'school_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['student.School']))
        db.execute("ALTER TABLE student_student ALTER COLUMN school_id TYPE integer USING (school_id::integer);")
        # Adding index on 'Student', fields ['school']
        db.create_index(u'student_student', ['school_id'])


    def backwards(self, orm):
        # Removing index on 'Student', fields ['school']
        db.delete_index(u'student_student', ['school_id'])

        # Deleting model 'School'
        db.delete_table(u'student_school')


        # Renaming column for 'Student.school' to match new field type.
        db.rename_column(u'student_student', 'school_id', 'school')
        # Changing field 'Student.school'

        for student in orm['student.Student'].objects.all():
            if student.school == 1180:
                student.school = 'BOSC'
            if student.school == 1188:
                student.school = 'BRAN'
            if student.school == 1203:
                student.school = 'BWRN'
            if student.school == 1221:
                student.school = 'CALT'
            if student.school == 1262: 
                student.school = 'CMU_'
            if student.school == 1267:
                student.school = 'CWRU'
            if student.school == 1387:
                student.school = 'CW_M'
            if student.school == 1403:
                student.school = 'COLU'
            if student.school == 1430:
                student.school = 'CORN'
            if student.school == 123:
                student.school = 'DART'
            if student.school == 169:
                student.school = 'DUKE'
            if student.school == 215:
                student.school = 'EMRY'
            if student.school == 288:
                student.school = 'GRGE'
            if student.school == 291:
                student.school = 'GTCH'
            if student.school == 1462:
                student.school = 'HRVD'
            if student.school == 384:
                student.school = 'JHU_'
            if student.school == 424:
                student.school = 'LHGH'
            if student.school == 1583:
                student.school = 'MIT_'
            if student.school == 527:
                student.school = 'NYU_'
            if student.school == 570:
                student.school = 'NRTH'
            if student.school == 1787:
                student.school = 'PRIN'
            if student.school == 651:
                student.school = 'RICE'
            if student.school == 1997:
                student.school = 'STAN'
            if student.school == 749:
                student.school = 'TUFT'
            if student.school == 823:
                student.school = 'UCLA'
            if student.school == 826:
                student.school = 'UCSD'
            if student.school == 827:
                student.school = 'UCSF'
            if student.school == 836:
                student.school = 'UCHI'
            if student.school == 906:
                student.school = 'MICH'
            if student.school == 941:
                student.school = 'UNC_'
            if student.school == 955:
                student.school = 'NRTD'
            if student.school == 2047:
                student.school = 'PENN'
            if student.school == 2073:
                student.school = 'URCH'
            if student.school == 2084:
                student.school = 'USC_'
            if student.school == 2132:
                student.school = 'UVA_'
            if student.school == 2145:`
                student.school = 'WISC'
            if student.school == 966:
                student.school = 'VAND'
            if student.school == 990:
                student.school = 'WAKE'
            if student.school == 1012:
                student.school = 'WUSL'
            if student.school == 2159:
                student.school = 'YALE'
            if student.school == 2165:
                student.school = 'OTHR'

            student.save()
        #db.alter_column(u'student_student', 'school', self.gf('django.db.models.fields.CharField')(max_length=50))
        db.execute("ALTER TABLE student_student ALTER COLUMN school TYPE varchar USING (school_id::varchar);")

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
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['student.School']"}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['student.Skill']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'year_in_school': ('django.db.models.fields.CharField', [], {'default': "'FR'", 'max_length': '2'})
        }
    }

    complete_apps = ['student']
