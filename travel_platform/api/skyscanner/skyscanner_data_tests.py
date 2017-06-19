import unittest

from skyscanner_data import SkyscannerData

# FIXME: Sasha: Fix all these tests, they fails because of invalid parameters.


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
        expected_result = {u'Carriers': [{u'CarrierId': 230, u'Name': u'VietJet Air'},
                           {u'CarrierId': 843, u'Name': u'AirAsia'},
                           {u'CarrierId': 1044, u'Name': u'Ethiopian Airlines'},
                           {u'CarrierId': 1193, u'Name': u'Uzbekistan Airways'},
                           {u'CarrierId': 1281, u'Name': u'Jetstar'},
                           {u'CarrierId': 1416, u'Name': u'Malaysia Airlines'},
                           {u'CarrierId': 1417, u'Name': u'SilkAir'},
                           {u'CarrierId': 1426, u'Name': u'Malindo Air'},
                           {u'CarrierId': 1713, u'Name': u'Singapore Airlines'},
                           {u'CarrierId': 1762, u'Name': u'Scoot/Tigerair'}],
             u'Currencies': [{u'Code': u'GBP',
                              u'DecimalDigits': 2,
                              u'DecimalSeparator': u'.',
                              u'RoundingCoefficient': 0,
                              u'SpaceBetweenAmountAndSymbol': False,
                              u'Symbol': u'\xa3',
                              u'SymbolOnLeft': True,
                              u'ThousandsSeparator': u','}],
             u'Dates': [[None, {u'DateString': u'2017-07-15'}],
                        [{u'DateString': u'2017-07-18'},
                         {u'MinPrice': 40.0, u'QuoteDateTime': u'2017-06-15T12:58:00'}]],
             u'Places': [{u'CityId': u'KULM',
                          u'CityName': u'Kuala Lumpur',
                          u'CountryName': u'Malaysia',
                          u'IataCode': u'KUL',
                          u'Name': u'Kuala Lumpur International',
                          u'PlaceId': 64012,
                          u'SkyscannerCode': u'KUL',
                          u'Type': u'Station'},
                         {u'CityId': u'SINS',
                          u'CityName': u'Singapore',
                          u'CountryName': u'Singapore',
                          u'IataCode': u'SIN',
                          u'Name': u'Singapore Changi',
                          u'PlaceId': 81870,
                          u'SkyscannerCode': u'SIN',
                          u'Type': u'Station'}]}

        self.assertEqual(actual_result, expected_result)
