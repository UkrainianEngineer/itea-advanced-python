import unittest
from config_reader import get_setting


class TestExample(unittest.TestCase):

    def test_get_item(self):
        cfg_file = '../travel_platform/travel_app/config/configurations.cfg'
        section = 'api.open.map'
        parameter = 'API_URL'
        self.assertEqual(get_setting(cfg_file, section, parameter),
                         'http://open.mapquestapi.com/geocoding/v1/reverse')

if __name__ == '__main__':
    unittest.main()
