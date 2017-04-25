import ConfigParser
from urlparse import urlparse

config = ConfigParser.RawConfigParser()
result_parse = urlparse('https://ru.foursquare.com/')
print(result_parse)
config.add_section('scheme')
config.add_section('netloc')
config.add_section('path')
config.add_section('params')
config.add_section('query')
config.add_section('fragment')

config.set('scheme', result_parse.scheme)
config.set('netloc', result_parse.netloc)
config.set('path', result_parse.path)
config.set('params', result_parse.params)
config.set('query', result_parse.query)
config.set('fragment', result_parse.fragment)

with open ('confile_foursquare.ini', 'w') as configfile:
	config.write(configfile)
