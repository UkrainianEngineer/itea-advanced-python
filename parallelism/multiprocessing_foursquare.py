import os
import requests
from time import time
import urllib
import multiprocessing

venues = "https://api.foursquare.com/v2/venues/search?v=20170101&near=Lviv&query=coffee&client_id=VXYTEYOX4NYHJVAOVFCKFGKSDYWJXZBH0TDLZSPGYEAL1M1B&client_secret=21PSW4AMQIZMJR3MTQXGFUCUXGJPDBWVXQRLVXPE2SPXBC0V"
vanue_photos = "https://api.foursquare.com/v2/venues/%s/photos?v=20161016&client_id=VXYTEYOX4NYHJVAOVFCKFGKSDYWJXZBH0TDLZSPGYEAL1M1B&client_secret=21PSW4AMQIZMJR3MTQXGFUCUXGJPDBWVXQRLVXPE2SPXBC0V"

response = requests.get(venues)
data = response.json()
ts = time()

def process_data(venue):
    venue_name = venue["name"]
    venue_id = venue["id"]
    print venue_name
    photos_response = requests.get(vanue_photos % venue_id)
    items_data =  photos_response.json()["response"]["photos"]["items"]
    for item in items_data:
        user_photo = item["user"]["photo"]
        photo_url = user_photo["prefix"] + "original" + user_photo["suffix"]
        folder_name = "photos/%s/%s_%s/" % (venue_name,
                                            item["user"]["firstName"],
                                            item["user"].get("lastName"))
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        urllib.urlretrieve(photo_url, folder_name + user_photo["suffix"])
        print folder_name

processes = multiprocessing.Pool(10)
processes.map(process_data, data["response"]["venues"])
print("Took {}".format(time() - ts))

