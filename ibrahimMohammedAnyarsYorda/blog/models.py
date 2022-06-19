from django.contrib.auth import get_user_model
from django.db import models
from django.forms import DateTimeField
from django.utils.translation import gettext as _
# Create your models here.


class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_text = models.TextField((""))
    post_author = get_user_model()
    created_date = models.DateTimeField(
        (""), auto_now=False, auto_now_add=False)
    published_date = models.DateTimeField(
        (""), auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.post_title
