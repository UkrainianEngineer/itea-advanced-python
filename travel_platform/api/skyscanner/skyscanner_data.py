from skyscanner.skyscanner import FlightsCache
from conf import config

api_key = config.get('api_skyscanner', 'api_key')
flights_cache_service = FlightsCache(api_key)

data = {"market": "UK", "currency": "GBP", "locale": "en-GB",
        "originplace": "SIN-sky", "destinationplace": "KUL-sky",
        "outbounddate": "2017-07-15", "inbounddate": "2017-07-18"}


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

