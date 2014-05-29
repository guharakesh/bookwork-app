from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employer(models.Model):
    user = models.OneToOneField(User,null=True)

    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos',blank=True)
    description = models.CharField(max_length=255)
    logoURL = models.URLField(default='/static/img/default_employer.png')
    companyURL = models.URLField(default='http://www.example.com')


    def __unicode__(self):
        return u"%s" % self.name

