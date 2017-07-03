# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
import sys

from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from api.izi_travel.izi_travel_data import *
from config.conf import CONF_PATH


# FIXME RomanPryima: remade sys path in a properly way
sys.path.append('../../config_parser/')
sys.path.append('./config')


def index(request):
    return render(request, 'travel_app/main.html')


def coord(request):
    """
    This view receives coordinates of location from the GET request, sends it
    to the Open Maps API. Than returns name of the location received from API
    to the frontend.

    :param request: data received from frontend, containing longitude and
      latitude
    :return: name of location gotten from open maps API.
    to
    """

    api_section = 'api.open.map'

    api_url = get_setting(CONF_PATH, api_section, 'API_URL')
    api_key = get_setting(CONF_PATH, api_section, 'API_KEY')
    coordinate_lon = request.GET.get('lon')
    coordinate_lat = request.GET.get('lat')
    location = ','.join([coordinate_lat, coordinate_lon])
    params = {'key': api_key, 'location': location}

    location_request = requests.get(api_url, params=params)
    location_data = location_request.json()

    response = location_data['results'][0]['locations'][0]['adminArea5']
    response = response.encode('utf-8')
    return JsonResponse(response, safe=False)


@cache_page(settings.CACHE_MIDDLEWARE_SECONDS)
def get_city_tourist_info(request):
    city = request.GET['desired_location']
    data = get_museums_with_tours(city)
    museums = data["museums"]
    tours = data["tours"]
    context = {'museums': museums, 'tours': tours, 'city': city}
    return render(request, 'travel_app/search.html', context=context)


@cache_page(settings.CACHE_MIDDLEWARE_SECONDS)
def museum_detail(request, id_, lang):
    detail = find_museum_detail(id_, languages=lang)
    return render(request, 'travel_app/museum_detail.html',
                  context={'detail': detail})


@cache_page(settings.CACHE_MIDDLEWARE_SECONDS)
def tour_detail(request, id_, lang):
    detail = find_tour_attractions(id_, languages=lang)
    return render(request, 'travel_app/tour_detail.html',
                  context={'detail': detail})


def get_available_cities_from_izi_travel(request):
    city = request.GET['search']
    cities = client.search_city_by_name(city)
    return JsonResponse(cities, safe=False)
# TODO: try to use different api to get list of cities(google for ex)
