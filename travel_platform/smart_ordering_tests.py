import unittest

from smart_ordering import smart_ordering


class SmartOrderingTest(unittest.TestCase):
    def setUp(self):
        self.data = [{"country": "United States", "city": "San-Francisco",
                      "rating": 4.89},
                     {"country": "Spain", "city": "Madrid", "rating": 4.85},
                     {"country": "Ukraine", "city": "Lviv", "rating": 5.0}]

        self.data2 = [{'name': 'Pavlo', 'age': 27, 'gender': 'male'},
                      {'name': 'Kate', 'age': 28, 'gender': 'female'},
                      {'name': 'Duc', 'age': 48, 'gender': 'male'},
                      {'name': 'Duc1', 'age': 48, 'gender': 'male'},
                      {'name': 'Duc', 'age': 45, 'gender': 'male'},
                      {'name': 'Sasha'},
                      {'name': 'Sasha1'},
                      {'name': 'Sasha2'},
                      {'age': 60},
                      {'age': 10},
                      {'age': 20},
                      {'name': 'Roman', 'gender': 'male'}]

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

    def test_smart_ordering_filter_age_desc_not_existing_key(self):
        actual_result = smart_ordering(self.data2, filter_by="age",
                                       order_by="desc")
        expected_result = [{'age': 60},
                           {'gender': 'male', 'age': 48, 'name': 'Duc'},
                           {'gender': 'male', 'age': 48, 'name': 'Duc1'},
                           {'gender': 'male', 'age': 45, 'name': 'Duc'},
                           {'gender': 'female', 'age': 28, 'name': 'Kate'},
                           {'gender': 'male', 'age': 27, 'name': 'Pavlo'},
                           {'age': 20},
                           {'age': 10},
                           {'name': 'Sasha'},
                           {'name': 'Sasha1'},
                           {'name': 'Sasha2'},
                           {'gender': 'male', 'name': 'Roman'}]

        self.assertEqual(actual_result, expected_result)

    def test_smart_ordering_filter_age_asc_not_existing_key(self):
        actual_result = smart_ordering(self.data2, filter_by="age",
                                       order_by="asc")
        expected_result = [{'age': 10},
                           {'age': 20},
                           {'gender': 'male', 'age': 27, 'name': 'Pavlo'},
                           {'gender': 'female', 'age': 28, 'name': 'Kate'},
                           {'gender': 'male', 'age': 45, 'name': 'Duc'},
                           {'gender': 'male', 'age': 48, 'name': 'Duc'},
                           {'gender': 'male', 'age': 48, 'name': 'Duc1'},
                           {'age': 60},
                           {'name': 'Sasha'},
                           {'name': 'Sasha1'},
                           {'name': 'Sasha2'},
                           {'gender': 'male', 'name': 'Roman'}]

        self.assertEqual(actual_result, expected_result)
