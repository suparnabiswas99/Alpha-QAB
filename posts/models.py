from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 120)
    #tags = TaggableManager(manager=_CustomTaggableManager())
    brief = models.CharField(max_length=120,null=True)
    content = RichTextUploadingField(max_length=1000000,null=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})

    class Meta:
        ordering = ["-timestamp", "-updated"]

'''

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)
'''

def upload_location(instance, filename):
    PostModel = instance.__class__
    new_id = PostModel.objects.order_by("id").last().id + 1
    """
    instance.__class__ gets the model Post. We must use this method because the model is defined below.
    Then create a queryset ordered by the "id"s of each object, 
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.
    """
    return "%s/%s" %(new_id, filename)

class Profile(models.Model):
    user = models.OneToOneField(User,related_name='profile', on_delete=models.CASCADE)
    bio = models.CharField(max_length=140,)
    gender = models.IntegerField(choices=(
                                        (1, "MALE"),
                                        (2, "FEMALE"),
                                        (3, "OTHER"),
                                        ))
    pic = models.ImageField(upload_to=upload_location,
                                        null=True,
                                        blank=True,
                                        width_field="width_field",
                                        height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __str__(self):
        return 'Profile of user: {}'.format(self.user.username)





