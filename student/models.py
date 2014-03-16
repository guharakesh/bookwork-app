from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db.models import BooleanField
from social_auth.models import UserSocialAuth
import urllib2
# import code for encoding urls and generating md5 hashes
# needed for gravatar
import urllib, hashlib

# Create your models here.

class Skill(models.Model):

    students = models.ManyToManyField('Student', through='SkillStudent',blank=True)

    skill_text = models.CharField(max_length=200)

    approved = BooleanField(default=False, blank=True)
    creator = models.ForeignKey(User, related_name='creator', null=True, blank=True)

    def __unicode__(self):
        return u"%s" % self.skill_text

def upload_to(instance, filename):
    return 'images/%s/%s' % (instance.user.user.username, filename)

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

    profile_pic = models.ImageField(upload_to=upload_to, default = 'pic_folder/None/no-img.jpg')

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

    def getPictureURL(self):
        try:
            social_info = UserSocialAuth.objects.get(user=self.user);
            if social_info.provider == 'facebook':
                url = "http://graph.facebook.com/"+social_info.uid+"/picture?width=100&height=100"
                req = urllib2.Request(url)
                res = urllib2.urlopen(req)
                return res.geturl()
            elif social_info.provider == 'linkedin':
                return social_info.extra_data['picture-url']
            else:
                # if they have social but no facebook or linkedin it gets here
                return '/static/img/default.png'
        except:
            # if not in social_auth then this is what runs
            # redbull image right now
            # Set your variables here
            email = self.user.email
            default = '/static/img/default.png'
            # "https://openclipart.org/image/300px/svg_to_png/190113/1389952697.png"
            size = 40
             
            # construct the url
            gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
            gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
            return gravatar_url
        else:
            # the last catch. shouldn't hit this. (right now a redbull image from facebook)
            return '/static/img/default.png'


class SkillStudent(models.Model):
    skill = models.ForeignKey(Skill)
    student = models.ForeignKey(Student)

    class Meta:
        db_table = 'student_skill_students'
        auto_created = Skill

class Employer(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos',blank=True)
    description = models.CharField(max_length=255)

    def __unicode__(self):
        return u"%s" % self.name

