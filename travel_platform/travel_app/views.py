# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse

from django.conf import settings
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from api.izi_travel.izi_travel_data import *


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


# @cache_page(settings.CACHE_MIDDLEWARE_SECONDS)
def get_city_tourist_info(request):
    city = request.GET['desired_location']
    museums = find_museums(city)
    tours = find_city_tours(city)
    context = {'museums': museums, 'tours': tours, 'city': city}
    return render(request, 'travel_app/search.html', context=context)


# @cache_page(settings.CACHE_MIDDLEWARE_SECONDS)
def museum_detail(request, id_, lang):
    detail = find_museum_detail(id_, languages=lang)
    return render(request, 'travel_app/museum_detail.html',
                  context={'detail': detail})


# @cache_page(settings.CACHE_MIDDLEWARE_SECONDS)
def tour_detail(request, id_, lang):
    detail = find_tour_attractions(id_, languages=lang)
    return render(request, 'travel_app/tour_detail.html',
                  context={'detail': detail})
