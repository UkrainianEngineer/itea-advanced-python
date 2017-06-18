import unittest

from skyscanner_data import SkyscannerData

# FIXME: which parameters there are must be expected? FAILED (errors=4)

class SkyscannerDataTest(unittest.TestCase):
    def setUp(self):
        self.data = {"market": "UK", "currency": "GBP", "locale": "en-GB",
                     "originplace": "SIN-sky", "destinationplace": "KUL-sky",
                     "outbounddate": "2017-07-15", "inbounddate": "2017-07-16"}


    def test_cheapest_quotes(self):
        actual_result = SkyscannerData.cheapest_quotes(**self.data)
        expected_result = {}

        self.assertEqual(actual_result, expected_result)

    def test_cheapest_price_by_route(self):
        actual_result = SkyscannerData.cheapest_price_by_route(**self.data)
        expected_result = {}

        self.assertEqual(actual_result, expected_result)

    def test_cheapest_price_by_date(self):
        actual_result = SkyscannerData.cheapest_price_by_date(**self.data)
        expected_result = {}

        self.assertEqual(actual_result, expected_result)

    def test_grid_prices_by_date(self):
        actual_result = SkyscannerData.grid_prices_by_date(**self.data)
        expected_result = {}

        self.assertEqual(actual_result, expected_result)
