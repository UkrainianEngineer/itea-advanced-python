import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read('config.cfg')

print (Config.get('SectionOne', 'Value'))
print (Config.get('SectionTwo', 'FavoriteColor'))
