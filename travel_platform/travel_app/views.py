# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests

import sys

from django.http import Http404

from django.http import JsonResponse

from django.shortcuts import render

from config_parser.config_reader import get_setting

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
