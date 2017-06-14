# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.cache import cache
from django.shortcuts import render

from api.izi_travel.izi_travel_data import *


def index(request):
    return render(request, 'travel_app/main.html')


def get_city_tourist_info(request):
    city = request.GET['desired_location']
    info = cache.get(city)

    if not info:
        museums = find_museums(city)
        tours = find_city_tours(city)
        cache.set(city, {"museums": museums, "tours": tours})
        context = {'museums': museums, 'tours': tours, 'city': city}
    else:
        museums = info.get("museums")
        tours = info.get("tours")
        context = {'museums': museums, 'tours': tours, 'city': city}
    return render(request, 'travel_app/search.html', context=context)


def museum_detail(request, id):
    detail = cache.get(id)

    if not detail:
        detail = find_museum_detail(id)
        cache.set(id, detail)
    return render(request, 'travel_app/museum_detail.html',
                  context={'detail': detail})


def tour_detail(request, id):
    detail = cache.get(id)
    if not detail:
        detail = find_tour_attractions(id)
        cache.set(id, detail)
    return render(request, 'travel_app/tour_detail.html',
                  context={'detail': detail})
