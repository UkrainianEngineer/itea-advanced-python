import os
import requests
from time import time
import urllib
from Queue import Queue
from threading import Thread

venues = "https://api.foursquare.com/v2/venues/search?v=20170101&near=Lviv&query=coffee&client_id=VXYTEYOX4NYHJVAOVFCKFGKSDYWJXZBH0TDLZSPGYEAL1M1B&client_secret=21PSW4AMQIZMJR3MTQXGFUCUXGJPDBWVXQRLVXPE2SPXBC0V"
vanue_photos = "https://api.foursquare.com/v2/venues/%s/photos?v=20161016&client_id=VXYTEYOX4NYHJVAOVFCKFGKSDYWJXZBH0TDLZSPGYEAL1M1B&client_secret=21PSW4AMQIZMJR3MTQXGFUCUXGJPDBWVXQRLVXPE2SPXBC0V"

response = requests.get(venues)
data = response.json()
ts = time()
queue = Queue()


class DownloadWorker(Thread):
   def __init__(self, queue):
       Thread.__init__(self)
       self.queue = queue

   def run(self):
       while True:
           # Get the work from the queue and expand the tuple
           venue = self.queue.get()
           process_data(venue)
           self.queue.task_done()

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


for thread in range(10):
    worker = DownloadWorker(queue)
    worker.daemon = True
    worker.start()

for venue in data["response"]["venues"]:
    queue.put((venue))
queue.join()
print("Took {}".format(time() - ts))

