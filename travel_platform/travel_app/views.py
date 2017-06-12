# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404

from django.http import JsonResponse

from django.shortcuts import render

from .models import Query


def index(request):
    return render(request, 'travel_app/main.html')


def coord(request):
    """
    View added for checking of interaction of map from landing page with 
    server.
    :param request: 
    :return: 
    """
    if 'lon' in request.GET:
        lon = request.GET['lon']
        lat = request.GET['lat']
        response = lon + " " + lat
    else:
        response = 'Venues are not found'
    return JsonResponse(response, safe=False)
