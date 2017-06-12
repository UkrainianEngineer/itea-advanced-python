import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from skyscanner.skyscanner import FlightsCache
from conf import config


class SkyscannerApiClient(object):

    api_key = config.get('api_skyscanner', 'api_key')
    market = config.get('api_skyscanner', 'market')
    currency = config.get('api_skyscanner', 'currency')
    locale = config.get('api_skyscanner', 'locale')
    origin_place = config.get('api_skyscanner', 'origin_place')
    destination_place = config.get('api_skyscanner', 'destination_place')
    outbound_date = config.get('api_skyscanner', 'outbound_date')
    inbound_date = config.get('api_skyscanner', 'inbound_date')

    flights_cache_service = FlightsCache(api_key)

    def __init__(self, api_key, market, currency, locale, origin_place,
                 destination_place, outbound_date, inbound_date):
        self.api_key = api_key
        self.market = market
        self.currency = currency
        self.locale = locale
        self.origin_place = origin_place
        self.destination_place = destination_place
        self.outbound_date = outbound_date
        self.inbound_date = inbound_date


    def cheapest_quotes(self):
        result = flights_cache_service.get_cheapest_quotes()
        return result


print SkyscannerApiClient.cheapest_quotes()


# sys.path.pop()
