from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from .choices import GENDER_CHOICES

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    bio = models.CharField(max_length=140)
    gender = models.IntegerField(choices=GENDER_CHOICES,default=1)
    pic = models.ImageField(upload_to = 'static/posts/images/user_pics/', default = 'static/posts/images/default.jpg')

    def __str__(self):
        return 'Profile of user: {}'.format(self.user.username)

class Post(models.Model):
    title = models.CharField(max_length = 120)
    brief = models.CharField(max_length=120,null=True)
    content = RichTextUploadingField(max_length=10000,null=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    author = models.ForeignKey(User,null=True)

    def __str__(self):
        return self.title

class Tag:
    tag_no = models.IntegerField()
    post = models.ForeignKey(Post, null=True)