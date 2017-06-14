import requests

from conf import CONF_PATH
from config_parser.config_reader import get_setting


class BaseExceptionHandler(Exception):
    """Base class for client exceptions."""
    pass


class IziTravelApiError(BaseExceptionHandler):
    pass


class BaseIziTravelApiClient(object):
    API_URL = get_setting(CONF_PATH, 'api.izi.travel', 'API_URL')
    API_VERSION = get_setting(CONF_PATH, 'api.izi.travel', 'API_VERSION')
    MEDIA_URL = get_setting(CONF_PATH, 'api.izi.travel', 'MEDIA_URL')
    LANGUAGES = get_setting(CONF_PATH, 'api.izi.travel', 'LANGUAGES')

    def __init__(self, api_key):
        if not api_key:
            raise ValueError("API key must be provided")
        self.api_key = api_key
        self.headers = {"X-IZI-API-KEY": self.api_key}

    def _check_response_status(self, response):
        """
        Raise an exception if status of a
         response from IziTravel is not 200.
        Args:
            response (obj): Response object.
        """
        if response.status_code != 200:
            raise IziTravelApiError("Status: {}. Response: {}.".format(
                response.status_code, response.content))

    def _prepare_image_url(self, content_provider_uuid,
                           image_uuid, image_size='480x360'):
        """
        Args:
            content_provider_uuid (str): Uuid of a content's provider.
            image_uuid (str): Uuid of an image.
            image_size (str): Image size. Available image sizes are:
            1600 x1200, 800 x600, 480 x360, 240 x180, 120x90.
        Returns:
            str: Image url.
        """
        data = {"media_url": self.MEDIA_URL, "provider": content_provider_uuid,
                "image": image_uuid, "size": image_size}
        image_url = "{media_url}/{provider}/{image}_{size}.jpg".format(**data)
        return image_url

    def _prepare_base_url(self, url):
        data = {"base_url": self.API_URL, "url": url}
        return "{base_url}/{url}/".format(**data)

    def _prepare_audio_url(self, content_provider_uuid, audio_uuid):
        """
        Args:
            content_provider_uuid (str): Uuid of a content's provider.
            audio_uuid (str): Uuid of an audio.
        Returns:
            str: Audio url.
        """
        data = {"media_url": self.MEDIA_URL,
                "provider": content_provider_uuid, "audio": audio_uuid}
        audio_url = '{media_url}/{provider}/{audio}.m4a'.format(**data)
        return audio_url

    def _prepare_params(self, **kwargs):
        """
        Args:
            **kwargs: Url parameters.
        Returns:
            dict: Url parameters.
        """
        params = {'version': self.API_VERSION, "languages": self.LANGUAGES}
        params.update(kwargs)
        return params

    def _make_request(self, service_url, **params):
        response = requests.get(service_url,
                                headers=self.headers, params=params)
        self._check_response_status(response)
        return response.json()


class IziTravelApiClient(BaseIziTravelApiClient):
    CITY_ENDPOINT = 'cities'
    CITY_CHILDREN_ENDPOINT = 'cities/{city_uuid}/children'
    MUSEUM_ENDPOINT = 'mtgobjects/{museum_uuid}'
    TOUR_ENDPOINT = 'mtgobjects/{tour_uuid}'
    ATTRACTION_ENDPOINT = 'mtgobjects/{attr_uuid}'
    REVIEW_ENDPOINT = 'mtgobjects/{obj_uuid}/reviews'
    FEATURED_ENDPOINT = 'featured'
    SEARCH_ENDPOINT = "mtg/objects/search"

    def get_city_uuid(self, city):
        """
        Args:
            city (str): City title.
        Returns:
            str: City uuid.
        """
        return self.get_city_by_name(city).get('city_uuid')

    def search_city_by_name(self, query):
        """
        Search for cities.
        Query example: "Ams".
        Response example:
        [
        {..., u'title':u'Amstelveen', u'map':{ u'bounds': ... },
            u'hash':..., u'uuid': u'..', u'language':u'en',
            u'children_count':1, u'location': { u'latitude':..,
            u'country_uuid':.., u'altitude':..,
            u'country_code':u'nl', u'longitude':..}, u'type':u'city'},
        {..., u'title':u'Amsterdam', u'map':{ u'bounds': ... },
            u'hash':..., u'uuid':u'..', u'language':u'en',
            u'children_count':1, u'location':{ u'latitude':..,
            u'country_uuid':.., u'altitude':.., u'country_code':u'nl',
            u'longitude':..}, u'type':u'city'},
        {..., u'title':u'Ouderkerk aan de Amstel', u'map':{ u'bounds': ... },
            u'hash':..., u'uuid':u'..', u'language':u'en',
            u'children_count':1, u'location':{ u'latitude':..,
            u'country_uuid':.., u'altitude':..,
            u'country_code':u'nl', u'longitude':..}, u'type':u'city'}
      ]
        Args:
            query (str): City name.
        Returns:
            list: Suggested cities.
        """
        url = self._prepare_base_url(self.SEARCH_ENDPOINT)
        prepared_params = {"type": "city", "query": query}
        params = self._prepare_params(**prepared_params)
        response = self._make_request(url, **params)
        return response

    def get_city_by_name(self, city):
        """
        Get certain city by exact name.
        Args:
            city (str): City name.
        Returns:
            dict: City data.
        """
        cities = self.search_city_by_name(city)
        city = {}

        if cities:

            city_data = cities.pop()
            city.update({
                "city_uuid": city_data.get("uuid", ""),
                # Number of tours and museums.
                "children_count": city_data.get("children_count", 0),
                "map": city_data.get("map", {}),
                "title": city_data.get("title", ""),
                # Coordinates, country code and uuid.
                "location": city_data.get("location", {})
            })
        return city

    def get_city_museums(self, city):
        """
        Get list of city museums with count of children:
        exhibits and collections.
        Args:
            city (str): City name.
        Returns:
            list: List of museums.
        """
        city_uuid = self.get_city_uuid(city)
        museums = []

        if city_uuid:

            params = self._prepare_params(**{"type": "museum"})
            url = self._prepare_base_url(self.CITY_CHILDREN_ENDPOINT.format(
                city_uuid=city_uuid))
            museums_data = self._make_request(url, **params)

            if museums_data:

                for museum in museums_data:
                    content_provider_uuid = (museum.get("content_provider",
                                                        {}).get("uuid", ""))
                    images = museum.get("images", [])
                    images_uuid = images[0].get("uuid", "") if images else ""
                    image_url = self._prepare_image_url(
                        content_provider_uuid, images_uuid)
                    mus = {
                        "image_url": image_url,
                        "title": museum.get("title", ""),
                        "museum_uuid": museum.get("uuid", ""),
                        "language": museum.get("language", ""),
                        "map": museum.get("map", {}),
                        "location": museum.get("location", {})
                    }
                    museums.append(mus)

        return museums

    def get_city_tours(self, city):
        """
        Get list of city tours.
        Args:
            city (str): City name.
        Returns:
            list: List of tours.
        """
        city_uuid = self.get_city_uuid(city)
        tours = []

        if city_uuid:

            url = self._prepare_base_url(self.CITY_CHILDREN_ENDPOINT.format(
                city_uuid=city_uuid))
            params = self._prepare_params()
            city_data = self._make_request(url, **params)

            if city_data:

                for obj in city_data:
                    if obj.get("type") == "tour":
                        city_tour = {
                            "tour_uuid": obj.get("uuid", ""),
                            "title": obj.get("title", ""),
                            "language": obj.get("language", ""),
                            "content_provider": obj.get("content_provider",
                                                        {}),
                            "reviews": obj.get("reviews", {}),
                            "location": obj.get("location", {}),
                            "images": []
                        }
                        for image in obj["images"]:
                            image_url = self._prepare_image_url(
                                city_tour["content_provider"]["uuid"],
                                image['uuid'])
                            city_tour["images"].append(image_url)
                        tours.append(city_tour)
        return tours

    def get_cities_with_content_on_requested_languages(self, languages=None):
        """
        Get list of cities that have content on requested languages.
        Args:
            languages (str): Requested languages.
        Returns:
            list: List of cities.
        """
        url = self._prepare_base_url(self.CITY_ENDPOINT)
        if languages is None:
            params = self._prepare_params()
        else:
            params = self._prepare_params(languages=languages)
        cities_data = self._make_request(url, **params)
        cities = []
        if cities_data:
            for city in cities_data:
                city_title = city.get("title", "")
                city_uuid = city.get("uuid", "")
                cities.append({"city_title": city_title,
                               "city_uuid": city_uuid})

        return cities

    def get_museum_detail_with_audio(self, museum_uuid):
        """
        Get details about museum with audio, reviews, description.
        Example response:
        [
        {u'status': u..', u'map': {...}, u'hash': u'...', u'uuid': '.',
            u'city': {u'status': u'published', u'map': {..},
            u'hash': u'...', u'uuid': u'...', u'language': u'uk',
            u'title': u'Title', u'summary': u'', u'languages': [u'ru',
            u'uk'], ..., u'location': {}, u'type': u'city'},
            u'content_provider': {...}, u'schedule': {u'wed':
            [u'10:00', u'16:30'], u'sun': [u'10:00', u'16:30']...},
            u'contacts': {u'phone_number': u'...', u'website': ..,
            u'address': u'..', u'city': u'..', u'country': u'ua'},
            u'languages': [u'ru', u'uk'],
            u'reviews': {u'rating_average': 10, u'reviews_count': 0,
            u'ratings_count': 1},
            u'location': {...}, u'content': [{u'language': u'uk',
            u'title': u'..', u'summary': u'', u'download': {u'map-mbtiles':
            {u'url': u'..', u'size': .., u'updated_at': u'..',
            u'md5': u'..'}}, u'images': [{..}], u'audio': [{...}],
             u'desc': u'...'}], u'type': u'museum', u'size': 12870139}
            ]
        Args:
            museum_uuid (str): Museum uuid.
        Returns:
            dict: Details about certain museum.
        """
        url = self._prepare_base_url(self.MUSEUM_ENDPOINT.format(
            museum_uuid=museum_uuid))
        prepared_params = {"includes": "download,city",
                           "except": "publisher,children"}
        params = self._prepare_params(**prepared_params)
        response = self._make_request(url, **params)
        detail_museum_info = {}

        if response:
            museum_data = response.pop()
            content_provider = museum_data.get("content_provider", {})
            content_provider_uuid = content_provider.get("uuid", "")
            content = museum_data.get("content", []).pop()
            audio = content.get("audio", [])
            audio_uuid = audio[0].get("uuid", "") if audio else ""
            detail_museum_info.update({
                "name": content_provider.get("name", ""),
                "audio": self._prepare_audio_url(content_provider_uuid,
                                                 audio_uuid),
                "description": content.get("desc", ""),
                "address": museum_data.get("contacts", {}),
                "reviews": museum_data.get("reviews", {}),
                "images": []

            })
            images = content.get("images", [])

            for image in images:
                im_url = self._prepare_image_url(content_provider_uuid,
                                                 image.get("uuid", ""))
                detail_museum_info["images"].append(im_url)

        return detail_museum_info

    def get_tourist_attractions(self, tour_uuid, params=None):
        """
        Get list of tourist attractions included in a tour.
        Example response:
        [
        {"status": .., "category": .., "placement": "..",
        "uuid": "...", "distance": "..", "country": {...},
        "languages": [..], "reviews": {..}, "map": {...},
        "duration": ..., "content": [
            {"language": "..", "title": "...", "playback": "..."},
            "images": [{..}, {..}], "children": [
            {...}, {...}, {...}]
            ]
        ]
        Args:
            tour_uuid (str): Tour uuid.
            params (dict): Any additional url parameters.
        Returns:
            list: Tourist attractions.
        """
        url = self._prepare_base_url(self.TOUR_ENDPOINT.format(
            tour_uuid=tour_uuid))

        if params is None:
            prepared_params = {"includes": "all,city,country",
                               "except": "translations,publisher,download"}
            params = self._prepare_params(**prepared_params)
        response = self._make_request(url, **params)
        tourist_attractions = []

        if response:

            tour_data = response.pop().get("content", []).pop()
            for child in tour_data.get("children", []):
                tour_title = tour_data.get('title', '')

                if child.get("type") == "tourist_attraction":
                    attraction = {
                        "tour_title": tour_title,
                        "title": child.get("title", ""),
                        "description": child.get("desc", ""),
                        "location": child.get("location", {}),
                        "language": child.get("language", ""),
                        "images": [],
                        "attr_uuid": child.get("uuid", ""),
                        "audio": ""
                    }
                    attraction["audio"] = self.get_tourist_attraction_audio(
                        attraction["attr_uuid"])
                    images = child.get("images", [])
                    content_provider = child.get("content_provider",
                                                 {}).get("uuid", "")
                    for image in images:
                        image_url = self._prepare_image_url(
                            content_provider, image["uuid"]
                        )
                        attraction["images"].append(image_url)
                    tourist_attractions.append(attraction)
        return tourist_attractions

    def get_tourist_attraction_audio(self, attraction_uuid):
        url = self._prepare_base_url(self.ATTRACTION_ENDPOINT.format(
            attr_uuid=attraction_uuid))
        params = self._prepare_params(**{"except": "city,country,publisher"})
        response = self._make_request(url, **params)
        audio_url = ""
        if response:
            tour_data = response.pop()
            content_provider = tour_data.get("content_provider",
                                             "").get("uuid", "")
            audio = tour_data.get("content", []).pop()["audio"].pop()["uuid"]
            audio_url = self._prepare_audio_url(content_provider, audio)
        return audio_url

    def get_object_reviews_and_rating(self, obj_uuid):
        """
        General method for getting reviews on any object by uuid.
        Args:
            obj_uuid (str): Object uuid.
        Returns:
            dict: Reviews info.
        """
        url = self._prepare_base_url(self.REVIEW_ENDPOINT.format(
            obj_uuid=obj_uuid))
        params = self._prepare_params()
        response = self._make_request(url, **params)

        if response:
            reviews = response.get("metadata", {})
            return reviews

        return {}

    def get_featured_content(self):
        """
        Returns:
            dict: Website featured content.
        """
        url = self._prepare_base_url(self.FEATURED_ENDPOINT)
        params = self._prepare_params()
        response = self._make_request(url, **params)
        return response
