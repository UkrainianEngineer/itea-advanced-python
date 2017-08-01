import unittest
from skyscanner_data import *
import datetime


class SkyscannerDataTest(unittest.TestCase):
    def setUp(self):
        outbounddate = (datetime.date.today() +
                        datetime.timedelta(7)).strftime('%Y-%m-%d')
        inbounddate = (datetime.date.today() +
                       datetime.timedelta(30)).strftime('%Y-%m-%d')
        self.data = {"market": "UK", "currency": "GBP", "locale": "en-GB",
                     "originplace": "SIN-sky", "destinationplace": "KUL-sky",
                     "outbounddate": outbounddate, "inbounddate": inbounddate}

    def test_cheapest_quotes_if_keys_in(self):
        result = cheapest_quotes(self.data)
        keys = ['Carriers', 'Currencies', 'Places', 'Quotes']
        self.assertTrue(all([key in result for key in keys]))

    def test_cheapest_price_by_route_if_keys_in(self):
        result = cheapest_price_by_route(self.data)
        keys = ['Carriers', 'Currencies', 'Places', 'Quotes']
        self.assertTrue(all([key in result for key in keys]))

    def test_cheapest_price_by_date_if_keys_in(self):
        result = cheapest_price_by_date(self.data)
        keys = ['Carriers', 'Currencies', 'Places', 'Quotes']
        self.assertTrue(all([key in result for key in keys]))

    def test_grid_prices_by_date_if_keys_in(self):
        result = grid_prices_by_date(self.data)
        keys = ['Carriers', 'Currencies', 'Places', 'Dates']
        self.assertTrue(all([key in result for key in keys]))

    def test_grid_prices_by_date_if_key_not(self):
        result = grid_prices_by_date(self.data)
        key = 'Quotes'
        self.assertFalse(key in result)
