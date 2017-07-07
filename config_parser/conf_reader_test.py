import unittest
from config_reader import get_setting



class TestExample(unittest.TestCase):

    def test_get_item(self):
        cfg_file = 'config_parser/test_data/configurations.cfg'
        section = 'api.open.map'
        parameter = 'API_URL'
        self.assertEqual(get_setting(cfg_file, section, parameter),
                         'http://example.com')

if __name__ == '__main__':
    unittest.main()
