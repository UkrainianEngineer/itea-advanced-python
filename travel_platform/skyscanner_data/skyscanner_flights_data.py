from skyscanner import Flights

flights_service = Flights('API key')

result = flights_service.get_result(
    country='UK',
    currency='GBP',
    locale='en-GB',
    originplace='SIN-sky',
    destinationplace='KUL-sky',
    outbounddate='2017-06-28',
    inbounddate='2017-06-31',
    adults=1).parsed

print(result)
