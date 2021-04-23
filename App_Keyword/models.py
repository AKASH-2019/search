from django.db import models
from datetime import datetime, date
# Create your models here.
from search_engine import settings



class Keyword(models.Model):
    name = models.CharField(max_length=264, blank=True)
    count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created', ]

    def __str__(self):
        return self.name


class KeywordSearch(models.Model):
    page = models.ForeignKey(Keyword, on_delete=models.CASCADE, related_name='searchPage')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="userSearch")
    date = models.DateTimeField(auto_now_add=True)
    start = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    end = models.DateField(auto_now_add=True, auto_now=False, blank=True)

    class Meta:
        ordering = ['-date', ]

    # def __str__(self):
    #     return self.user

class Bookmark(models.Model):
    page = models.ForeignKey(Keyword, on_delete=models.CASCADE, related_name='bookmarkPage')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookmarkUser')

    def __str__(self):
        return '{} : {}'.format(self.user, self.page)

