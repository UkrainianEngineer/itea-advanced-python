import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from skyscanner.skyscanner import FlightsCache
from conf import config

api_key = config.get('api_skyscanner', 'api_key')

flights_cache_service = FlightsCache(api_key)

#FIXME: why my *kwargs not work? TypeError: get_cheapest_quotes() takes exactly 1 argument (2 given)

def cheapest_quotes(**kwargs):
    return flights_cache_service.get_cheapest_quotes(kwargs).parsed

# print flights_cache_service.get_cheapest_quotes(market = 'UK', currency = 'GBP', locale = 'en-GB',
#                       originplace = 'SIN-sky', destinationplace = 'KUL-sky',
#                       outbounddate = '2017-07-15', inbounddate = '2017-07-18').parsed

def cheapest_price_by_route(**kwargs):
    return flights_cache_service.get_cheapest_price_by_route(kwargs).parsed


def cheapest_price_by_date(**kwargs):
    return flights_cache_service.get_cheapest_price_by_date(kwargs).parsed


def grid_prices_by_date(**kwargs):
    return flights_cache_service.get_grid_prices_by_date(kwargs).parsed

print cheapest_quotes(market = 'UK', currency = 'GBP', locale = 'en-GB',
                      originplace = 'SIN-sky', destinationplace = 'KUL-sky',
                      outbounddate = '2017-07-15', inbounddate = '2017-07-18')

print cheapest_price_by_route(market = 'UK', currency = 'GBP', locale = 'en-GB',
                      originplace = 'SIN-sky', destinationplace = 'KUL-sky',
                      outbounddate = '2017-07-15', inbounddate = '2017-07-18')

print cheapest_price_by_date(market = 'UK', currency = 'GBP', locale = 'en-GB',
                      originplace = 'SIN-sky', destinationplace = 'KUL-sky',
                      outbounddate = '2017-07-15', inbounddate = '2017-07-18')

print grid_prices_by_date(market = 'UK', currency = 'GBP', locale = 'en-GB',
                      originplace = 'SIN-sky', destinationplace = 'KUL-sky',
                      outbounddate = '2017-07-15', inbounddate = '2017-07-18')

sys.path.pop()
