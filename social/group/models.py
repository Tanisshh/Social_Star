from django.db import models

from django.utils.text import slugify
from django.urls import reverse
import misaka
import mistune

from django.contrib.auth import get_user_model
from django import template

register = template.Library()

User = get_user_model()

class Group(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description =  models.TextField(blank=True, default='')
    description_html = models.TextField(editable=True, default='', blank=True)
    member = models.ManyToManyRel(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('group:single',kwargs{'slug':self.slug})

    class Meta:
        ordering = ['name']


class GroupMember(models.Model):
    user = models.ForeignKey(User, related_name='user_group')
    group = models.ForeignKey(Group, related_name='memberships')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')
