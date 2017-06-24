import foursquare

from conf import CONF_PATH
from config_parser.config_reader import get_setting


client = foursquare.Foursquare(
    client_id=get_setting(CONF_PATH, "api.foursquare", "API_ID"),
    client_secret=get_setting(CONF_PATH, "api.foursquare", "API_SECRET"))


def find_venue(city):
    return client.venues.explore(params={'near': city})
