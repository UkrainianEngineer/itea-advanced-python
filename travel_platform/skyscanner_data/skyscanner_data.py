import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from skyscanner.skyscanner import FlightsCache
from conf import config

api_key = config.get('api_skyscanner', 'api_key')
flights_cache_service = FlightsCache(api_key)

data = {"market": "UK", "currency": "GBP", "locale": "en-GB",
        "originplace": "SIN-sky", "destinationplace": "KUL-sky",
        "outbounddate": "2017-07-15", "inbounddate": "2017-07-18"
}

class SkyscannerData(object):

    def __init__(self, params):
        self.params = params

    def cheapest_quotes(self):
        result = flights_cache_service.get_cheapest_quotes(**self.params).parsed
        return result


    def cheapest_price_by_route(self):
        result = flights_cache_service.get_cheapest_price_by_route(**self.params).parsed
        return result


    def cheapest_price_by_date(self):
        result = flights_cache_service.get_cheapest_price_by_date(**self.params).parsed
        return result


    def grid_prices_by_date(self):
        result = flights_cache_service.get_grid_prices_by_date(**self.params).parsed
        return result

sys.path.pop()

# D = SkyscannerData(data)
# from pprint import pprint
# print(D.grid_prices_by_date())