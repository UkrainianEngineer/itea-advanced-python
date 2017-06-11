# coding=utf-8
import requests
import unittest

from conf import CONF_PATH
from config_parser.config_reader import get_setting
from izi_travel_client import IziTravelApiClient, IziTravelApiError


class IziTravelTest(unittest.TestCase):
    def setUp(self):
        self.client = IziTravelApiClient(api_key=get_setting(CONF_PATH,
                                                             'api.izi.travel',
                                                             'API_KEY'))
        self.city = "Lviv"

    def test_get_city_by_name_returns_city(self):
        result = self.client.get_city_by_name(self.city)
        keys = ["title", "location", "map", "children_count", "city_uuid"]
        self.assertTrue(all([key in result for key in keys]))
        self.assertEqual(len(result.get("city_uuid")), 36)

    def test_get_unexisting_city_returns_empty_dict(self):
        result = self.client.get_city_by_name('Unknown city')
        self.assertEqual(result, {})

    def test_get_city_museums_returns_museums(self):
        result = self.client.get_city_museums(self.city)
        self.assertTrue(len(result) > 0)
        self.assertEquals(requests.get(result[0]["image_url"]).status_code,
                          200)

    def test_unexisting_city_museums_returns_empty_list(self):
        result = self.client.get_city_museums('Unknown city')
        self.assertEqual(result, [])

    def test_get_city_tours(self):
        result = self.client.get_city_tours(self.city)
        self.assertTrue(len(result) > 0)

    def test_unexisting_city_tours_returns_empty_list(self):
        result = self.client.get_city_tours("Unexisitng")
        self.assertEqual(result, [])

    def test_get_cities_with_content_on_requested_languages(self):
        result = self.client.get_cities_with_content_on_requested_languages(
            languages='uk')
        self.assertTrue(len(result) > 0)
        self.assertIn("city_title", result[0])
        self.assertIn("city_uuid", result[0])
        self.assertIn(u"Львів", [city.get("city_title") for city in result])

    def test_get_museum_detail_with_audio(self):
        museum_uuid = "cd8f9805-0efc-4360-92b1-d21bba446542"
        result = self.client.get_museum_detail_with_audio(museum_uuid)
        keys = ["name", "audio", "description", "address", "reviews", "images"]
        self.assertTrue(all([key in result for key in keys]))
        self.assertEquals(requests.get(result["audio"]).status_code,
                          200)

    def test_get_unexisting_museum_raises_error(self):
        museum_uuid = "unexisting_museum_uuid"
        self.assertRaises(IziTravelApiError,
                          self.client.get_museum_detail_with_audio,
                          museum_uuid)

    def test_get_tourist_attractions(self):
        tour_uuid = 'f1d66e34-c4e9-4139-8d49-865329e2427f'
        result = self.client.get_tourist_attractions(tour_uuid)
        self.assertTrue(len(result) > 0)
        keys = ["title", "description", "location", "language", "images",
                "attr_uuid"]
        self.assertTrue(all([key in result[0] for key in keys]))

    def test_get_object_review_and_rating(self):
        obj_uuid = 'f1d66e34-c4e9-4139-8d49-865329e2427f'
        result = self.client.get_object_reviews_and_rating(obj_uuid)
        self.assertIn('rating_average', result)
