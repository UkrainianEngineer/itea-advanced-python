from multiprocessing.pool import ThreadPool

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


def get_city_object_worker(params):
    """
    Get list of city objects. Worker for thread.
    Possible object types are: museums, tours.
    Args:
         params (tuple): City name, object type.
    Returns:
        tuple: object type (str), result (list of objects).
    """
    city, obj_type = params
    result = []
    if obj_type == "museums":
        result = find_museums(city)
    elif obj_type == "tours":
        result = find_city_tours(city)
    return obj_type, result


def get_museums_with_tours(city):
    """
    Get all the city objects (museums, tours) in parallel.
    Args:
        city (str): City name.
    Returns:
        dict: city objects in a structure like:
            {
            "museums": [museum1, museum2, ...],
            "tours": [tour1, tour2, ..]
            }

    """
    pool = ThreadPool(processes=2)
    data = pool.map(get_city_object_worker, [(city, obj_type)
                                             for obj_type in
                                             ["museums", "tours"]])
    return dict(data)
