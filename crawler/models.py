from django.db import models

# Create your models here.


class Word(models.Model):
    word = models.CharField(verbose_name="단어", null=False)
    category = models.ForeignKey(verbose_name="카테고리", null=False, on_delete=models.CASCADE())
    source = models.TextField()


class Category(models.Model):
    name = models.CharField(verbose_name="카테고리 명")
    source = models.URLField(verbose_name="출처")
