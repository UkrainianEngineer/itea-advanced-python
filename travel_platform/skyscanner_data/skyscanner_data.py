from skyscanner.skyscanner import FlightsCache

from travel_platform.conf import config


class SkyscannerApiClient(object):
    API_URL = config.get('api_skyscanner', 'API_URL')
    API_VERSION = config.get('api_skyscanner', 'API_VERSION')
    MEDIA_URL = config.get('api_skyscanner', 'MEDIA_URL')
    LANGUAGES = config.get('api_skyscanner', 'LANGUAGES')

    def __init__(self, api_key):
        if not api_key:
            raise ValueError("API key must be provided")
        self.api_key = api_key

    def flights_cache_service(self,
                              market='UK',
                              currency='GBP',
                              locale='en-GB',
                              originplace='SIN-sky',
                              destinationplace='KUL-sky',
                              outbounddate='2017-07-15',
                              inbounddate='2017-07-18'):

        flights_cache_service = FlightsCache(self.api_key)
        return flights_cache_service.get_cheapest_quotes(market,
                                                         currency,
                                                         locale,
                                                         originplace,
                                                         destinationplace,
                                                         outbounddate,
                                                         inbounddate).parsed

response = SkyscannerApiClient(api_key=config.get('api_skyscanner', 'API_KEY'))
print response
