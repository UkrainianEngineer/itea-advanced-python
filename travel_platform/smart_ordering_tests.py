import unittest

from smart_ordering import smart_ordering


class SmartOrderingTest(unittest.TestCase):
    def setUp(self):
        self.data = [{"country": "United States", "city": "San-Francisco",
                      "rating": 4.89},
                     {"country": "Spain", "city": "Madrid", "rating": 4.85},
                     {"country": "Ukraine", "city": "Lviv", "rating": 5.0}]

    def test_smart_ordering_sorted(self):
        actual_result = smart_ordering(self.data)
        expected_result = sorted(self.data)
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_not_existing_key(self):
        actual_result = smart_ordering(self.data, "salary")
        expected_result = [{"country": "United States",
                            "city": "San-Francisco", "rating": 4.89},
                           {"country": "Spain", "city": "Madrid",
                            "rating": 4.85},
                           {"country": "Ukraine", "city": "Lviv",
                            "rating": 5.0}
                           ]
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_country(self):
        actual_result = smart_ordering(self.data, filter_by="country")
        expected_result = [{"country": "Spain", "city": "Madrid",
                            "rating": 4.85},
                           {"country": "Ukraine", "city": "Lviv",
                            "rating": 5.0},
                           {"country": "United States",
                            "city": "San-Francisco", "rating": 4.89}
                           ]
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_country_asc(self):
        actual_result = smart_ordering(self.data, filter_by="country",
                                       order_by="asc")
        expected_result = [{"country": "Spain", "city": "Madrid",
                            "rating": 4.85},
                           {"country": "Ukraine", "city": "Lviv",
                            "rating": 5.0},
                           {"country": "United States",
                            "city": "San-Francisco", "rating": 4.89}
                           ]
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_country_asc_limit(self):
        actual_result = smart_ordering(self.data, filter_by="country",
                                       order_by="asc", limit=2)
        expected_result = [{"country": "Spain", "city": "Madrid",
                            "rating": 4.85},
                           {"country": "Ukraine", "city": "Lviv",
                            "rating": 5.0},
                           ]
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_country_asc_limit_over(self):
        actual_result = smart_ordering(self.data, filter_by="country",
                                       order_by="asc", limit=4)
        expected_result = [{"country": "Spain", "city": "Madrid",
                            "rating": 4.85},
                           {"country": "Ukraine", "city": "Lviv",
                            "rating": 5.0},
                           {"country": "United States",
                            "city": "San-Francisco", "rating": 4.89}
                           ]
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_country_asc_limit_zero(self):
        actual_result = smart_ordering(self.data, filter_by="country",
                                       order_by="asc", limit=0)
        expected_result = []
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_country_desc(self):
        actual_result = smart_ordering(self.data, filter_by="country",
                                       order_by="desc")
        expected_result = [{"country": "United States",
                            "city": "San-Francisco", "rating": 4.89},
                           {"country": "Ukraine", "city": "Lviv",
                            "rating": 5.0},
                           {"country": "Spain", "city": "Madrid",
                            "rating": 4.85},
                           ]
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_country_desc_limit(self):
        actual_result = smart_ordering(self.data, filter_by="country",
                                       order_by="desc", limit=2)
        expected_result = [{"country": "United States",
                            "city": "San-Francisco", "rating": 4.89},
                           {"country": "Ukraine", "city": "Lviv",
                            "rating": 5.0},
                           ]
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_country_desc_limit_over(self):
        actual_result = smart_ordering(self.data, filter_by="country",
                                       order_by="desc", limit=4)
        expected_result = [{"country": "United States",
                            "city": "San-Francisco", "rating": 4.89},
                           {"country": "Ukraine", "city": "Lviv",
                            "rating": 5.0},
                           {"country": "Spain", "city": "Madrid",
                            "rating": 4.85},
                           ]
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_country_desc_limit_zero(self):
        actual_result = smart_ordering(self.data, filter_by="country",
                                       order_by="desc", limit=0)
        expected_result = []
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_city(self):
        actual_result = smart_ordering(self.data, filter_by="city")
        expected_result = [{"country": "Ukraine", "city": "Lviv",
                            "rating": 5.0},
                           {"country": "Spain", "city": "Madrid",
                            "rating": 4.85},
                           {"country": "United States",
                            "city": "San-Francisco", "rating": 4.89}
                           ]
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_city_asc(self):
        actual_result = smart_ordering(self.data, filter_by="city",
                                       order_by="asc")
        expected_result = [{"country": "Ukraine", "city": "Lviv",
                            "rating": 5.0},
                           {"country": "Spain", "city": "Madrid",
                            "rating": 4.85},
                           {"country": "United States",
                            "city": "San-Francisco", "rating": 4.89}
                           ]
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_city_asc_limit(self):
        actual_result = smart_ordering(self.data, filter_by="city",
                                       order_by="asc", limit=2)
        expected_result = [{"country": "Ukraine", "city": "Lviv",
                            "rating": 5.0},
                           {"country": "Spain", "city": "Madrid",
                            "rating": 4.85},
                           ]
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_city_asc_limit_over(self):
        actual_result = smart_ordering(self.data, filter_by="city",
                                       order_by="asc", limit=4)
        expected_result = [{"country": "Ukraine", "city": "Lviv",
                            "rating": 5.0},
                           {"country": "Spain", "city": "Madrid",
                            "rating": 4.85},
                           {"country": "United States",
                            "city": "San-Francisco", "rating": 4.89}
                           ]
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_city_asc_limit_zero(self):
        actual_result = smart_ordering(self.data, filter_by="city",
                                       order_by="asc", limit=0)
        expected_result = []
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_city_desc(self):
        actual_result = smart_ordering(self.data, filter_by="city",
                                       order_by="desc")
        expected_result = [{"country": "United States",
                            "city": "San-Francisco", "rating": 4.89},
                           {"country": "Spain", "city": "Madrid",
                            "rating": 4.85},
                           {"country": "Ukraine", "city": "Lviv",
                            "rating": 5.0},
                           ]
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_city_desc_limit(self):
        actual_result = smart_ordering(self.data, filter_by="city",
                                       order_by="desc", limit=2)
        expected_result = [{"country": "United States",
                            "city": "San-Francisco", "rating": 4.89},
                           {"country": "Spain", "city": "Madrid",
                            "rating": 4.85},
                           ]
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_city_desc_limit_over(self):
        actual_result = smart_ordering(self.data, filter_by="city",
                                       order_by="desc", limit=4)
        expected_result = [{"country": "United States",
                            "city": "San-Francisco", "rating": 4.89},
                           {"country": "Spain", "city": "Madrid",
                            "rating": 4.85},
                           {"country": "Ukraine", "city": "Lviv",
                            "rating": 5.0},
                           ]
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_city_desc_limit_zero(self):
        actual_result = smart_ordering(self.data, filter_by="city",
                                       order_by="desc", limit=0)
        expected_result = []
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_rating(self):
        actual_result = smart_ordering(self.data, filter_by="rating")
        expected_result = [{"country": "Spain", "city": "Madrid",
                            "rating": 4.85},
                           {"country": "United States",
                            "city": "San-Francisco", "rating": 4.89},
                           {"country": "Ukraine", "city": "Lviv",
                            "rating": 5.0}
                           ]
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_rating_asc(self):
        actual_result = smart_ordering(self.data, filter_by="rating",
                                       order_by="asc")
        expected_result = [{"country": "Spain", "city": "Madrid",
                            "rating": 4.85},
                           {"country": "United States",
                            "city": "San-Francisco", "rating": 4.89},
                           {"country": "Ukraine", "city": "Lviv",
                            "rating": 5.0}]
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_rating_asc_limit(self):
        actual_result = smart_ordering(self.data, filter_by="rating",
                                       order_by="asc", limit=2)
        expected_result = [{"country": "Spain", "city": "Madrid",
                            "rating": 4.85},
                           {"country": "United States",
                            "city": "San-Francisco", "rating": 4.89}
                           ]
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_rating_asc_limit_over(self):
        actual_result = smart_ordering(self.data, filter_by="rating",
                                       order_by="asc", limit=4)
        expected_result = [{"country": "Spain", "city": "Madrid",
                            "rating": 4.85},
                           {"country": "United States",
                            "city": "San-Francisco", "rating": 4.89},
                           {"country": "Ukraine", "city": "Lviv",
                            "rating": 5.0}]
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_rating_asc_limit_zero(self):
        actual_result = smart_ordering(self.data, filter_by="rating",
                                       order_by="asc", limit=0)
        expected_result = []
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_rating_desc(self):
        actual_result = smart_ordering(self.data, filter_by="rating",
                                       order_by="Desc")
        expected_result = [{"country": "Ukraine", "city": "Lviv",
                            "rating": 5.0},
                           {"country": "United States",
                            "city": "San-Francisco", "rating": 4.89},
                           {"country": "Spain", "city": "Madrid",
                            "rating": 4.85},
                           ]
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_rating_desc_limit(self):
        actual_result = smart_ordering(self.data, filter_by="rating",
                                       order_by="Desc", limit=2)
        expected_result = [{"country": "Ukraine", "city": "Lviv",
                            "rating": 5.0},
                           {"country": "United States",
                            "city": "San-Francisco", "rating": 4.89},
                           ]
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_rating_desc_limit_over(self):
        actual_result = smart_ordering(self.data, filter_by="rating",
                                       order_by="Desc", limit=4)
        expected_result = [{"country": "Ukraine", "city": "Lviv",
                            "rating": 5.0},
                           {"country": "United States",
                            "city": "San-Francisco", "rating": 4.89},
                           {"country": "Spain", "city": "Madrid",
                            "rating": 4.85}
                           ]
        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_rating_desc_limit_zero(self):
        actual_result = smart_ordering(self.data, filter_by="rating",
                                       order_by="Desc", limit=0)
        expected_result = []
        self.assertEqual(actual_result, expected_result)
