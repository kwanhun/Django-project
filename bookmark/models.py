from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=100, blank=True)
    url = models.URLField('URL', unique=True)
    # 사용자를 foreignkey로 할당하기 위한 field 생성
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    tags = TaggableManager(blank=True)
    def __str__(self):
        return self.title

