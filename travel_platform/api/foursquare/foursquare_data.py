import foursquare

from conf import CONF_PATH
from config_parser.config_reader import get_setting

foursquare_client = foursquare.Foursquare(
    client_id=get_setting(CONF_PATH, "api.foursquare", "API_ID"),
    client_secret=get_setting(CONF_PATH, "api.foursquare", "API_SECRET"))


def foursquare_find_venue(city, query='museum'):
    """
    Data of requested venues in desired city.
    :param city: str Name of the location given by view "get_city_tourist_info"
    :param query: str type of venues for searching.
    :return: A list of tuples containing id, name, address*, phone* and photo*
    of venues fonded in the city.
    * - if available.
    """
    city_venues_data = foursquare_client.venues.search(
        params={'near': city, 'query': query})
    venues_data = []
    for venue in city_venues_data['venues']:
        venue_id = venue.get('id')
        name = venue.get('name')
        url = venue.get('url')
        address = venue.get('location').get('address')
        phone = venue.get('contact').get('phone')
        photo = foursquare_venue_photos(venue_id)
        venue_data = dict(
            id=venue_id, name=name, url=url, address=address, phone=phone,
            photo=photo, )
        venues_data.append(venue_data)
    return venues_data


def foursquare_venue_photos(venue_id, size='cap500'):
    """
    Picture of requested venue.
    :param venue_id: str id of venue, provided by "foursquare_find_venue"
     function.
    :param size: str size of picture. By default - "cap500" - 500 pixels on the
                 larger dimension (width or height).
    :return: str url of photos of venue.
    """
    venue_data = foursquare_client.venues.photos(venue_id, params={})
    items = venue_data.get('photos').get('items')
    venue_photo = ''
    if items:
        venue_photo = items[0].get('prefix') + size + items[0].get('suffix')
    return venue_photo


def foursquare_explore_venues(city, query):
    """
    Returns a list of recommended venues near the current location.
    :param city: str City name.
    :param query: str type of venues for searching.
    :return: A list of dicts containing id, name, address, phone and photo
    of venues found in the city.
    """
    city_venues_data = foursquare_client.venues.explore(
        params={'near': city, 'query': query, 'venuePhotos': True})
    venues_data = []
    for venue_item in city_venues_data['groups'][0]['items']:
        venue = venue_item.get('venue', {})
        photo_groups = venue.get("photos", {}).get("groups", [])
        photo = ''
        if photo_groups:
            # Take only the very first picture.
            photo_prefix = photo_groups[0]['items'][0]['prefix']
            photo_suffix = photo_groups[0]['items'][0]['suffix']
            photo = '{prefix}{size}{suffix}'.format(
                prefix=photo_prefix, size='original', suffix=photo_suffix
            )
        venue_id = venue.get('id', '')
        name = venue.get('name', '')
        url = venue.get('url', '')
        address = venue.get('location', {}).get('address', '')
        phone = venue.get('contact', {}).get('phone', '')
        venue_data = dict(
            id=venue_id, name=name, url=url, address=address, phone=phone,
            photo=photo)
        venues_data.append(venue_data)
    return venues_data
