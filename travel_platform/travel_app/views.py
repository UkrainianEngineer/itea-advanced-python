# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404

from django.shortcuts import render

from .models import Query


def index(request):
    return render(request, 'travel_app/main.html')
