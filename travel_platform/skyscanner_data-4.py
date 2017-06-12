import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from skyscanner.skyscanner import FlightsCache
from conf import config

class SkyscannerApiClient(object):

    def __init__(self, api_key, market, currency, locale, origin_place,
                 destination_place, outbound_date, inbound_date):

        self.api_key = config.get('api_skyscanner', 'api_key')
        self.market = config.get('api_skyscanner', 'market')
        self.currency = config.get('api_skyscanner', 'currency')
        self.locale = config.get('api_skyscanner', 'locale')
        self.origin_place = config.get('api_skyscanner', 'origin_place')
        self.destination_place = config.get('api_skyscanner', 'destination_place')
        self.outbound_date = config.get('api_skyscanner', 'outbound_date')
        self.inbound_date = config.get('api_skyscanner', 'inbound_date')

    # def flights_cache_service(self):
    #
    #     flights_cache_service = FlightsCache(self.api_key)
    #     return flights_cache_service.get_cheapest_quotes().parsed


print SkyscannerApiClient
# response = SkyscannerApiClient()
# print response.flights_cache_service()
# sys.path.pop()
