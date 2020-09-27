# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Todo(models.Model):
  
    title = models.CharField(max_length=50, verbose_name='Başlık')
    completed = models.BooleanField(verbose_name='Durum')

    def __str__(self):
        return self.title
