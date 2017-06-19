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

    """TODO RomanPryima: make function sending coordinates and returning
    to the frontend name of location received from map API"""

    response = request.GET.get('lon') + " " + request.GET.get('lat')

    return JsonResponse(response, safe=False)
