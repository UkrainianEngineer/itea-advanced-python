import unittest
from skyscanner_data import *


class SkyscannerDataTest(unittest.TestCase):
    def setUp(self):
        self.data = {"market": "UK", "currency": "GBP", "locale": "en-GB",
                     "originplace": "SIN-sky", "destinationplace": "KUL-sky",
                     "outbounddate": "2017-07-15", "inbounddate": "2017-07-16"}

    def test_cheapest_quotes(self):
        response = cheapest_quotes(self.data)
        self.assertTrue(response)

    def test_cheapest_quotes_if_params_in(self):
        params = ['Carriers', 'Currencies', 'Places', 'Quotes']
        response = True
        for param in params:
            if param not in cheapest_quotes(self.data):
                response = False
                break
        self.assertTrue(response)

    def test_cheapest_price_by_route(self):
        response = cheapest_price_by_route(self.data)
        self.assertTrue(response)

    def test_cheapest_price_by_route_if_params_in(self):
        params = ['Carriers', 'Currencies', 'Places', 'Quotes']
        response = True
        for param in params:
            if param not in cheapest_quotes(self.data):
                response = False
                break
        self.assertTrue(response)

    def test_cheapest_price_by_date(self):
        response = cheapest_price_by_date(self.data)
        self.assertTrue(response)

    def test_grid_prices_by_date(self):
        response = grid_prices_by_date(self.data)
        self.assertTrue(response)
