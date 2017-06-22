from skyscanner.skyscanner import FlightsCache
from conf import config

api_key = config.get('api_skyscanner', 'api_key')
flights_cache_service = FlightsCache(api_key)

data = {"market": "UK", "currency": "GBP", "locale": "en-GB",
        "originplace": "SIN-sky", "destinationplace": "KUL-sky",
        "outbounddate": "2017-07-15", "inbounddate": "2017-07-18"}


print flights_cache_service.get_cheapest_quotes(**data).parsed

