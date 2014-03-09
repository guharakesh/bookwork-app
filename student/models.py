from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db.models import BooleanField

# Create your models here.

class Skill(models.Model):

    students = models.ManyToManyField('Student', through='SkillStudent',blank=True)

    skill_text = models.CharField(max_length=200)

    approved = BooleanField(default=False, blank=True)
    creator = models.ForeignKey(User, related_name='creator', null=True, blank=True)

    def __unicode__(self):
        return u"%s" % self.skill_text

class Student(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return u"%s" % self.user.email

    def date_joined(self):
        return self.user.date_joined

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def get_email(self):
        return self.user.email
        
    skills = models.ManyToManyField('Skill', through='SkillStudent')

    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior+'),
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
        ('CALT','California Institute of Technology'),
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
        ('MIT_','Massachusetts Institute of Technology'),
        ('NYU_','New York University'),
        ('NRTH','Northwestern University'),
        ('PRIN','Princeton University'),
        ('RICE','Rice University'),
        ('STAN','Stanford University'),
        ('TUFT','Tufts University'),
        ('UCLA','University of California, Los Angeles'),
        ('UCSD','University of California, San Diego'),
        ('UCSF','University of California, San Francisco'),
        ('UCHI','University of Chicago'),
        ('MICH','University of Michigan'),
        ('UNC_','University of North Carolina'),
        ('NTRD','University of Notre Dame'),
        ('PENN','University of Pennsylvania'),
        ('URCH','University of Rochester'),
        ('USC_','University of Southern California'),
        ('UVA_','University of Virginia'),
        ('WISC','University of Wisconsin-Madison'),
        ('VAND','Vanderbilt University'),
        ('WAKE','Wake Forest University'),
        ('WUSL','Washington University in Saint Louis'),
        ('YALE','Yale University'),
        ('OTHR','Other'))
    
    school = models.CharField(max_length=50,choices=SCHOOL_CHOICES,
                              default='CWRU')

class SkillStudent(models.Model):
    skill = models.ForeignKey(Skill)
    student = models.ForeignKey(Student)

    class Meta:
        db_table = 'student_skill_students'
        auto_created = Skill

class Employer(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos')
    description = models.CharField(max_length=255)

    def __unicode__(self):
        return u"%s" % self.name

