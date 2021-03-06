from django.db import models
from django.utils import timezone
from weibousers.models import WeiboUser
import os
import django_filters
def image_path(instance, filename):
    return 'images/{0}/{1}/{2}'.format(instance.place.pk, instance.created.strftime("/%Y/%m/%d/"), filename)

class Place(models.Model):
    name = models.CharField(db_index=True, max_length=120)
    poiid = models.CharField(db_index=True, max_length=120)
    province = models.PositiveSmallIntegerField(null=True, blank=True)
    city = models.PositiveSmallIntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.name

class SubPlace(models.Model):
    place =  models.ForeignKey(Place)
    name = models.CharField(db_index=True, max_length=120)
    poiid = models.CharField(db_index=True, max_length=120)

    def __unicode__(self):
        return self.name

class Post(models.Model):
    place =  models.ForeignKey(Place)
    sub_place =  models.ForeignKey(SubPlace, blank=True, null=True)
    user = models.ForeignKey(WeiboUser)
    weibo_id = models.BigIntegerField(null=True, blank=True, unique=True)
    created = models.DateTimeField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    weibo_img = models.URLField(max_length=150, blank=True, null=True)
    weibo_thumb_img = models.URLField(max_length=150, blank=True, null=True)
    category = models.ForeignKey('categories.Category', blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to=image_path)

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return '%s' % (self.pk,)


class PostFilter(django_filters.FilterSet):
    created = django_filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Post
        fields = ['place','category', 'created', 'user__province', 'user__city']
