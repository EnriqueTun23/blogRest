from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True, width_field='width_field', height_field='height_field')
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    publish = models.DateTimeField(auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    # user = models.ForeignKey(User, on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
    
    def __unicode__(self):
        return self.title

    def get_url(self):

        return reverse('detail', kwargs={'id': self.id})