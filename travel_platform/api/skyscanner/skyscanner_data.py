import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from skyscanner.skyscanner import FlightsCache
from conf import config

api_key = config.get('api_skyscanner', 'api_key')
flights_cache_service = FlightsCache(api_key)

data = {"market": "UK", "currency": "GBP", "locale": "en-GB",
        "originplace": "SIN-sky", "destinationplace": "KUL-sky",
        "outbounddate": "2017-07-15", "inbounddate": "2017-07-18"}


class SkyscannerData(object):

    @staticmethod
    def cheapest_quotes(params):
        result = flights_cache_service.get_cheapest_quotes(**params).parsed
        return result

    @staticmethod
    def cheapest_price_by_route(params):
        result = flights_cache_service.get_cheapest_price_by_route(**params).parsed
        return result

    @staticmethod
    def cheapest_price_by_date(params):
        result = flights_cache_service.get_cheapest_price_by_date(**params).parsed
        return result

    @staticmethod
    def grid_prices_by_date(params):
        result = flights_cache_service.get_grid_prices_by_date(**params).parsed
        return result

sys.path.pop()

D = SkyscannerData()
from pprint import pprint
pprint(D.grid_prices_by_date(data))
