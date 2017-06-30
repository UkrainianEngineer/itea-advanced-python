from config_parser.config_reader import get_setting
from conf import CONF_PATH
from izi_travel_client import IziTravelApiClient


client = IziTravelApiClient(api_key=get_setting(CONF_PATH,
                                                "api.izi.travel",
                                                "API_KEY"))


def find_museums(city):
    return client.get_city_museums(city)


def find_museum_detail(museum_uuid, languages=None):
    return client.get_museum_detail_with_audio(museum_uuid,
                                               languages=languages)


def find_city_tours(city):
    return client.get_city_tours(city)


def find_tour_attractions(tour_uuid, languages=None):
    return client.get_tourist_attractions(tour_uuid, languages=languages)
