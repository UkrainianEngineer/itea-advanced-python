import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from skyscanner.skyscanner import FlightsCache
from conf import config

API_SECTION = "api_skyscanner"

api_key = config.get('api_skyscanner', 'api_key')
flights_cache_service = FlightsCache(api_key)

data = {}

def update_params(data, sections):
    # Read configs from configuration file.
    for section in sections:
        data.update({section: config.get(API_SECTION, section)})

api_params = ["market", "currency", "locale", "originplace",
              "destinationplace", "outbounddate", "inbounddate"]

# Prepare parameters for using SkyScanner API.
update_params(data, api_params)


def cheapest_quotes(params):
    result = flights_cache_service.get_cheapest_quotes(**params).parsed
    return result


def cheapest_price_by_route(params):
    result = flights_cache_service.get_cheapest_price_by_route(**params).parsed
    return result


def cheapest_price_by_date(params):
    result = flights_cache_service.get_cheapest_price_by_date(**params).parsed
    return result


def grid_prices_by_date(params):
    result = flights_cache_service.get_grid_prices_by_date(**params).parsed
    return result

print cheapest_quotes(data)
print cheapest_price_by_route(data)
print cheapest_price_by_date(data)
print grid_prices_by_date(data)

sys.path.pop()
