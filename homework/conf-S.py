import ConfigParser
import os

print 'abspath: ' + os.path.abspath(__file__)
print 'abspath2: ' + os.path.abspath('configurations.cfg')
print 'dirname1: ' + os.path.dirname(__file__)
print 'dirname2: ' + os.path.dirname(os.path.abspath(__file__))
print 'join: ' + os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              'configurations.cfg')

CONF_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         'configurations.cfg')

CONF_PATH2 = os.path.abspath('configurations.cfg')

print 'CONF_PATH: ' + type(CONF_PATH)
print 'CONF_PATH2: ' + type(CONF_PATH2)
# config = ConfigParser.ConfigParser()
# print config.read(CONF_PATH)
