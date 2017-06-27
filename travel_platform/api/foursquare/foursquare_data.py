import foursquare

from conf import CONF_PATH
from config_parser.config_reader import get_setting

client = foursquare.Foursquare(
    client_id=get_setting(CONF_PATH, "api.foursquare", "API_ID"),
    client_secret=get_setting(CONF_PATH, "api.foursquare", "API_SECRET"))


def foursquare_find_venue(city, query='museum'):
    city_venues_data = client.venues.search(
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


def foursquare_venue_photos(venue_id, size='width500'):
    venue_data = client.venues.photos(venue_id, params={})
    items = venue_data.get('photos').get('items')
    venue_photo = ''
    if items:
        venue_photo = items[0].get('prefix') + size + items[0].get('suffix')
    return venue_photo
