from skyscanner.skyscanner import FlightsCache

api_key = 'ka775911102027919433182126616312'

flights_cache_service = FlightsCache(api_key)
result = flights_cache_service.get_cheapest_quotes(
    market='UK',
    currency='GBP',
    locale='en-GB',
    originplace='SIN-sky',
    destinationplace='KUL-sky',
    outbounddate='2017-06-15',
    inbounddate='2017-06-18').parsed

print(result)