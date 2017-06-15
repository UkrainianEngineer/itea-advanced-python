import unittest

from mock import Mock, patch

from izi_travel_client import IziTravelApiClient

def get_mocked_cities():
    return [{"uuid": 1, "children_count": 1,
             "map": {"test": "Add real map here."},
             "title": "First city goes here.",
             "location": {"lon": 100, "lat": 300},
            },
            {"uuid": 2, "children_count": 4,
             "map": {"test2": "Add real map here."},
             "title": "Second city goes here.",
             "location": {"lon": 500, "lat": -200},
            }
           ]

def get_mocked_museums():
    return [
            {"content_provider": {"uuid": 1},
             "images": [{"uuid": 1, "name": "img1.png"},
                        {"uuid": 2, "name": "img2.png"}],
             "language": "UKR",
             "map": {"map_key": "Please use real data"},
             "location": {"lon": 100, "lat": 500},
            }
           ]

class IziTravelApiClientTest(unittest.TestCase):
    def setUp(self):
        patch.object(IziTravelApiClient, 'search_city_by_name',
                     return_value=get_mocked_cities()).start()
        patch.object(IziTravelApiClient, 'get_city_uuid',
                     return_value=1).start()
        self.client = IziTravelApiClient(Mock())

    def test_get_city_by_name_all_related_cities_are_shown(self):
        result = self.client.get_city_by_name("Lviv")
        expected_result = [{"city_uuid": 1, "children_count": 1,
                            "map": {"test": "Add real map here."},
                            "title": "First city goes here.",
                            "location": {"lon": 100, "lat": 300},
                           },
                           {"uuid": 2, "children_count": 4,
                            "map": {"test2": "Add real map here."},
                            "title": "Second city goes here.",
                            "location": {"lon": 500, "lat": -200},
                           },
                          ]
        self.assertEqual(result, expected_result)

    def test_get_city_museums(self):
        patch.object(IziTravelApiClient, '_make_request',
                     return_value=get_mocked_museums()).start()
        result = self.client.get_city_museums("Lviv")
        print result
