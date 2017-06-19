# coding=utf-8
import requests
import unittest

from izi_travel_data import (find_city_tours, find_museums,
                             find_museum_detail, find_tour_attractions)


class IziTravelRealDataTest(unittest.TestCase):
    def setUp(self):

        self.city = "Lviv"

    def test_find_museums_returns_list(self):
        museums = find_museums(self.city)
        self.assertTrue(len(museums) > 1)
        for museum in museums:
            self.assertIn("title", museum)
            self.assertIn("image_url", museum)
            self.assertIn("museum_uuid", museum)
            self.assertIn("language", museum)
            self.assertIn("map", museum)
            self.assertIn("location", museum)
        self.assertEquals(requests.get(museums[0]["image_url"]).status_code,
                          200)

    def test_find_museum_detail_returns_museum_detail(self):
        museum_uuid = find_museums(self.city)[1]["museum_uuid"]
        museum_detail = find_museum_detail(museum_uuid)
        keys = ["audio", "description", "reviews", "address"]
        self.assertTrue(all([key in museum_detail for key in keys]))

    def test_find_city_tours_returns_list(self):
        city_tours = find_city_tours(self.city)
        self.assertTrue(len(city_tours) > 1)
        for tour in city_tours:
            self.assertIn("title", tour)
            self.assertIn("images", tour)
            self.assertIn("language", tour)
            self.assertIn("reviews", tour)
            self.assertIn("location", tour)
            self.assertIn("content_provider", tour)
            self.assertIn("tour_uuid", tour)
        self.assertEquals(requests.get(city_tours[0]["images"][0]).status_code,
                          200)

    def test_find_tour_attractions_returns_list(self):
        tour_uuid = find_city_tours(self.city)[0]["tour_uuid"]
        attractions = find_tour_attractions(tour_uuid)
        self.assertTrue(len(attractions) > 1)
        keys = ["title", "images", "description", "attr_uuid", "audio"]
        self.assertEquals(requests.get(attractions[0]["audio"]).status_code,
                          200)
        self.assertTrue(all([key in attractions[0] for key in keys]))
