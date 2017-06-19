import ConfigParser
import os


CONF_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         'configurations.cfg')

config = ConfigParser.ConfigParser()
config.read(CONF_PATH)
