from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
import select2.fields
import select2.models

# Create your models here.

class Skill(models.Model):

    students = models.ManyToManyField('Student', through='SkillStudent')

    skill_text = models.CharField(max_length=200)

    def __unicode__(self):
        return u"%s" % self.skill_text

class Student(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return u"%s" % self.user.email

    skills = models.ManyToManyField('Skill', through='SkillStudent')

    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    year_in_school = models.CharField(max_length=2,
                                      choices=YEAR_IN_SCHOOL_CHOICES,
                                      default=FRESHMAN)

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)

    SCHOOL_CHOICES =(
        ('BOSC','Boston College'),
        ('BRAN','Brandeis University'),
        ('BRWN','Brown University'),
        ('CALT','California Institute of Technology (Caltech)'),
        ('CMU_','Carnegie Mellon University'),
        ('CWRU','Case Western Reserve University'),
        ('CW_M','College of William and Mary'),
        ('COLU','Columbia University'),
        ('CORN','Cornell University'),
        ('DART','Dartmouth College'),
        ('DUKE','Duke University'),
        ('EMRY','Emory University'),
        ('GRGE','Georgetown University'),
        ('GTCH','Georgia Institute of Technology'),
        ('HRVD','Harvard University'),
        ('JHU_','Johns Hopkins University'),
        ('LHGH','Lehigh University'),
        ('MIT_','Massachusetts Institute of Technology (MIT)'),
        ('NYU_','New York University (NYU)'),
        ('NRTH','Northwestern University'),
        ('PRIN','Princeton University'),
        ('RICE','Rice University'),
        ('STAN','Stanford University'),
        ('TUFT','Tufts University'),
        ('UCLA','University of California - LA'),
        ('UCSD','University of California - SD'),
        ('UCSF','University of California - SF'),
        ('UCHI','University of Chicago'),
        ('MICH','University of Michigan Ann Arbor'),
        ('UNC_','University of North Carolina'),
        ('NTRD','University of Notre Dame'),
        ('PENN','University of Pennsylvania'),
        ('URCH','University of Rochester'),
        ('USC_','University of Southern California'),
        ('UVA_','University of Virginia'),
        ('WISC','University of Wisconsin - Madison'),
        ('VAND','Vanderbilt University'),
        ('WAKE','Wake Forest University'),
        ('WUSL','Washington University in Saint Louis'),
        ('YALE','Yale University'))
    
    school = models.CharField(max_length=50,choices=SCHOOL_CHOICES,
                              default='BOSC')

class SkillStudent(models.Model):
    skill = models.ForeignKey(Skill)
    student = models.ForeignKey(Student)

    class Meta:
        db_table = 'student_skill_students'
        auto_created = Skill
