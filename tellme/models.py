from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Comments(models.Model):
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{} - {}".format(self.profile,self.comment)


class info(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=300,default="No biography added yet")
    photo = models.URLField(verbose_name="Enter your photo URL", default='https://www.polyvore.com/cgi/img-thing?.out=jpg&size=l&tid=16560098')

    def __str__(self):
        return "Additional info of {}".format(self.user)
