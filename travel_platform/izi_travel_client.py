import requests


class BaseExceptionHandler(Exception):
    """Base class for client exceptions."""
    pass


class IziTravelApiError(BaseExceptionHandler):
    pass


class BaseIziTravelApiClient(object):

    API_URL = "https://api.izi.travel"
    API_VERSION = '1.2.4'
    MEDIA_URL = 'https://media.izi.travel'
    LANGUAGES = "uk,en,ru"

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
                           image_uuid, image_size='800x600'):
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
        return"{base_url}/{url}/".format(**data)

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
        return self.find_city_by_name(city).get('city_uuid')

    def find_city_by_name(self, query):
        """
        Request for city information.
        Args:
            query (str): City name.
        Returns:
            dict: City data.
        """

        url = self._prepare_base_url(self.SEARCH_ENDPOINT)
        prepared_params = {"type": "city", "query": query}
        params = self._prepare_params(**prepared_params)
        response = self._make_request(url, **params)
        city = {}

        if response:
            city_data = response[0]
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
                        tours.append(obj)
                return tours
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
        return cities

    def get_museum_detail_with_audio(self, museum_uuid):
        """
        Get details about museum with audio, reviews, description.
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
        museum_data = self._make_request(url, **params)
        detail_museum_info = {}

        if museum_data:

            content_provider = museum_data[0].get("content_provider", {})
            content_provider_uuid = content_provider.get("uuid", "")
            content = museum_data[0].get("content", [])[0]
            audio_uuid = content.get("audio", [])[0].get("uuid", "")
            detail_museum_info.update({
                "name": content_provider.get("name", ""),
                "audio": self._prepare_audio_url(content_provider_uuid,
                                                 audio_uuid),
                "description": content.get("desc", ""),
                "address": museum_data[0].get("contacts", {}),
                "reviews": museum_data[0].get("reviews", {}),
                "images": []

            })
            images = content.get("images", [])

            for image in images:
                im_url = self._prepare_image_url(content_provider_uuid,
                                                 image.get("uuid", ""))
                detail_museum_info["images"].append(im_url)
            return detail_museum_info
        return detail_museum_info

    def get_tourist_attractions(self, tour_uuid, params=None):
        """
        Get list of tourist attractions included in a tour.
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

            tour_data = response[0].get("content", [])[0]
            for child in tour_data.get("children", []):

                if child.get("type") == "tourist_attraction":
                    attraction = {
                        "title": child.get("title", ""),
                        "description": child.get("desc", ""),
                        "location": child.get("location", {}),
                        "language": child.get("language", ""),
                        "images": child.get("images", []),
                        "attr_uuid": child.get("uuid", "")
                    }
                    tourist_attractions.append(attraction)
            return tourist_attractions
        return tourist_attractions

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
        reviews = {}
        return reviews

    def get_featured_content(self):
        """
        Returns:
            dict: Website featured content.
        """
        url = self._prepare_base_url(self.FEATURED_ENDPOINT)
        params = self._prepare_params()
        response = self._make_request(url, **params)
        return response


# config = ConfigParser.ConfigParser()
# config.read('configurations.cfg')
# API_KEY = config.get('api.izi.travel', 'API_KEY')
# client = IziTravelApiClient(api_key=API_KEY)
# print (client.find_city_by_name("Lviv"))
# print client.get_city_museums("Lviv")[0]["image_url"]
# print client.get_city_tours("Lviv")[0]
# mus_uuid = client.get_city_museums("Lviv")[0]["museum_uuid"]
# print (mus_uuid)
# print client.get_museum_detail_with_audio(mus_uuid)
# for key, value in client.get_museum_detail_with_audio(mus_uuid).items():
#     print(key, value)
# tour_id = client.get_city_tours("Lviv")[0]["uuid"]
# print tour_id
# print client.get_tourist_attractions(tour_id)
# print client.get_object_reviews_and_rating(tour_id)
# print client.get_featured_content()[0]
# print client.get_cities_with_content_on_requested_languages("uk")
