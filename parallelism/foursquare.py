import os
import requests
import urllib

venues = "https://api.foursquare.com/v2/venues/search?v=20170101&near=Lviv&query=coffee&client_id=VXYTEYOX4NYHJVAOVFCKFGKSDYWJXZBH0TDLZSPGYEAL1M1B&client_secret=21PSW4AMQIZMJR3MTQXGFUCUXGJPDBWVXQRLVXPE2SPXBC0V"
vanue_photos = "https://api.foursquare.com/v2/venues/%s/photos?v=20161016&client_id=VXYTEYOX4NYHJVAOVFCKFGKSDYWJXZBH0TDLZSPGYEAL1M1B&client_secret=21PSW4AMQIZMJR3MTQXGFUCUXGJPDBWVXQRLVXPE2SPXBC0V"

response = requests.get(venues)
data = response.json()
for point in data["response"]["venues"]:
    venue_name = point["name"]
    venue_id = point["id"]
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

