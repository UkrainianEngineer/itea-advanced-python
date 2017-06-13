import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from skyscanner.skyscanner import FlightsCache
from conf import config

api_key = config.get('api_skyscanner', 'api_key')
market = config.get('api_skyscanner', 'market')
currency = config.get('api_skyscanner', 'currency')
locale = config.get('api_skyscanner', 'locale')
origin_place = config.get('api_skyscanner', 'origin_place')
destination_place = config.get('api_skyscanner', 'destination_place')
outbound_date = config.get('api_skyscanner', 'outbound_date')
inbound_date = config.get('api_skyscanner', 'inbound_date')
flights_cache_service = FlightsCache(api_key)


def cheapest_quotes():
    result = flights_cache_service.get_cheapest_quotes(
        market='UK',
        currency='GBP',
        locale='en-GB',
        originplace='SIN-sky',
        destinationplace='KUL-sky',
        outbounddate='2017-07-15',
        inbounddate='2017-07-16').parsed
    return result


def cheapest_price_by_route():
    result = flights_cache_service.get_cheapest_price_by_route(
        market='UK',
        currency='GBP',
        locale='en-GB',
        originplace='SIN-sky',
        destinationplace='KUL-sky',
        outbounddate='2017-07-15',
        inbounddate='2017-07-16').parsed
    return result


def cheapest_price_by_date():
    result = flights_cache_service.get_cheapest_price_by_date(
        market='UK',
        currency='GBP',
        locale='en-GB',
        originplace='SIN-sky',
        destinationplace='KUL-sky',
        outbounddate='2017-07-15',
        inbounddate='2017-07-16').parsed
    return result


def grid_prices_by_date():
    result = flights_cache_service.get_grid_prices_by_date(
        market='UK',
        currency='GBP',
        locale='en-GB',
        originplace='SIN-sky',
        destinationplace='KUL-sky',
        outbounddate='2017-07-15',
        inbounddate='2017-07-16').parsed
    return result

print cheapest_quotes()
print cheapest_price_by_route()
print cheapest_price_by_date()
print grid_prices_by_date()

sys.path.pop()
