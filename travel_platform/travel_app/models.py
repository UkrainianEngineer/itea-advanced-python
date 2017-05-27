# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Query(models.Model):
    """docstring for ClassName"""
    available_money = models.CharField(max_length=6)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.query_text
