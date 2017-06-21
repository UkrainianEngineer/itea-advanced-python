data = {"market": "UK", "currency": "GBP", "locale": "en-GB",
        "originplace": "SIN-sky", "destinationplace": "KUL-sky",
        "outbounddate": "2017-07-15", "inbounddate": "2017-07-18"}

def cheapest_quotes(params):
    # result = flights_cache_service.get_cheapest_quotes(**params).parsed
    # return result
    print **params

print cheapest_quotes(data)