# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.cache import cache_page


from api.izi_travel.izi_travel_data import *


def index(request):
    return render(request, 'travel_app/main.html')


@cache_page(settings.CACHE_MIDDLEWARE_SECONDS)
def get_city_tourist_info(request):
    city = request.GET['desired_location']
    museums = find_museums(city)
    tours = find_city_tours(city)
    context = {'museums': museums, 'tours': tours, 'city': city}
    return render(request, 'travel_app/search.html', context=context)


@cache_page(settings.CACHE_MIDDLEWARE_SECONDS)
def museum_detail(request, id_):
    detail = find_museum_detail(id_)
    return render(request, 'travel_app/museum_detail.html',
                  context={'detail': detail})


@cache_page(settings.CACHE_MIDDLEWARE_SECONDS)
def tour_detail(request, id_):
    detail = find_tour_attractions(id_)
    return render(request, 'travel_app/tour_detail.html',
                  context={'detail': detail})
