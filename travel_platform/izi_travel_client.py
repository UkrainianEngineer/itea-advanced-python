import requests


class BaseExceptionHandler(Exception):
    """Base class for client exceptions."""
    pass


class IziTravelApiError(BaseExceptionHandler):
    pass


class IziTravelClient(object):

    def __init__(self):
        self.api_key = "9ba66b8d-2bdc-4674-bdc4-3cc67e2c25af"
        self.api_url = "https://api.izi.travel/"
        self.headers = {"X-IZI-API-KEY": self.api_key}
        self.api_version = '1.2.4'
        self.media_url = 'https://media.izi.travel/'
        self.languages = "uk,en,ru"

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
        image_url = "{base_url}{provider}/{image}_{size}.jpg".format(
            base_url=self.media_url, provider=content_provider_uuid,
            image=image_uuid, size=image_size)
        return image_url

    def _prepare_audio_url(self, content_provider_uuid, audio_uuid):
        """
        Args:
            content_provider_uuid (str): Uuid of a content's provider.
            audio_uuid (str): Uuid of an audio.
        Returns:
            str: Audio url.
        """
        audio_url = "{base_url}{provider}/{audio}.m4a".format(
            base_url=self.media_url, provider=content_provider_uuid,
            audio=audio_uuid)
        return audio_url

    def _prepare_params(self, **kwargs):
        """
        Args:
            **kwargs: Url parameters.
        Returns:
            dict: Url parameters.
        """
        params = {'version': self.api_version, "languages": self.languages}
        params.update(kwargs)
        return params

    def get_city_uuid(self, city):
        return self.find_city_by_name(city).get('city_uuid')

    def find_city_by_name(self, query):
        """
        Request for city information.
        Args:
            query (str): City name.
        Returns:
            dict: City data.
        """
        url = '{base_url}mtg/objects/search'.format(base_url=self.api_url)
        prepared_params = {"type": "city", "query": query}
        params = self._prepare_params(**prepared_params)
        response = requests.get(url, params, headers=self.headers)
        city = {}
        self._check_response_status(response)
        if response.json():
            city_data = response.json()[0]
            city["city_uuid"] = city_data.get("uuid")
            # Number of tours and museums.
            city["children_count"] = city_data["children_count"]
            city["map"] = city_data["map"]
            city["title"] = city_data["title"]
            # Coordinates, country code and uuid.
            city["location"] = city_data["location"]
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
        prepared_params = {"type": "museum"}
        params = self._prepare_params(**prepared_params)
        url = '{base_url}cities/{city}/children'.format(
            base_url=self.api_url, city=city_uuid)
        response = requests.get(url, params, headers=self.headers)
        self._check_response_status(response)
        museums_data = response.json()
        museums = []
        if museums_data:
            for museum in museums_data:
                mus = {}
                content_provider_uuid = (museum.get("content_provider").
                                         get("uuid"))
                images_uuid = museum.get("images")[0]["uuid"]
                image_url = self._prepare_image_url(
                    content_provider_uuid, images_uuid)
                mus["title"] = museum.get("title")
                mus["museum_uuid"] = museum.get("uuid")
                mus["image_url"] = image_url
                mus["language"] = museum.get("language")
                mus["map"] = museum.get("map")
                mus["location"] = museum.get("location")
                museums.append(mus)
            return museums
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
        url = '{base_url}cities/{city}/children'.format(
            base_url=self.api_url, city=city_uuid)
        params = self._prepare_params()
        response = requests.get(url, params, headers=self.headers)
        self._check_response_status(response)
        tours = []
        city_data = response.json()
        if city_data:
            for obj in city_data:
                if obj.get("type") == "tour":
                    tours.append(obj)
            return tours
        return tours

    def get_museum_detail_with_audio(self, museum_uuid):
        """
        Get details about museum with audio, reviews, description.
        Args:
            museum_uuid (str): Museum uuid.
        Returns:
            dict: Details about certain museum.
        """
        # TODO kate: add default values for fields like this:
        # dict.get("field")
        # It helps to understand type of this field.
        # Also it helps to avoid some unexpected behaviour with `None` type.
        url = "{base_url}mtgobjects/{museum}".format(
            base_url=self.api_url, museum=museum_uuid)
        prepared_params = {"includes": "download,city",
                           "except": "publisher,children"}
        params = self._prepare_params(**prepared_params)
        response = requests.get(url, params, headers=self.headers)
        self._check_response_status(response)
        museum_data = response.json()
        detail_museum_info = {}
        if museum_data:
            content_provider = museum_data[0].get("content_provider")
            detail_museum_info["name"] = content_provider.get("name")
            content_provider_uuid = content_provider.get("uuid")
            content = museum_data[0]["content"][0]
            audio_uuid = content["audio"][0]["uuid"]
            audio_url = self._prepare_audio_url(content_provider_uuid,
                                                audio_uuid)
            detail_museum_info["audio"] = audio_url
            description = content["desc"]
            detail_museum_info["description"] = description
            detail_museum_info["address"] = museum_data[0].get("contacts")
            images = content["images"]
            detail_museum_info["reviews"] = museum_data[0].get("reviews")
            detail_museum_info["images"] = museum_data[0].get("images", [])
            for image in images:
                im_url = self._prepare_image_url(content_provider_uuid,
                                                 image.get("uuid"))
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
        url = "{base_url}mtgobjects/{tour}".format(
            base_url=self.api_url, tour=tour_uuid)
        if params is None:
            prepared_params = {"includes": "all,city,country",
                               "except": "translations,publisher,download"}
            params = self._prepare_params(**prepared_params)
        response = requests.get(url, params, headers=self.headers)
        self._check_response_status(response)
        tourist_attractions = []
        if response.json():
            tour_data = response.json()[0]["content"][0]
            for child in tour_data["children"]:
                attraction = {}
                if child.get("type") == "tourist_attraction":
                    attraction["title"] = child["title"]
                    attraction["description"] = child["desc"]
                    attraction["location"] = child["location"]
                    attraction["language"] = child["language"]
                    attraction["images"] = child["images"]
                    attraction["attr_uuid"] = child["uuid"]
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
        url = "{base_url}mtgobjects/{obj}/reviews".format(
            base_url=self.api_url, obj=obj_uuid)
        params = self._prepare_params()
        response = requests.get(url, params, headers=self.headers)
        self._check_response_status(response)
        if response.json():
            reviews = response.json().get("metadata")
            return reviews
        reviews = {}
        return reviews

    def get_featured_content(self):
        """
        Returns:
            Website featured content.
        """
        url = "{}featured".format(self.api_url)
        params = self._prepare_params()
        response = requests.get(url, params, headers=self.headers)
        self._check_response_status(response)
        return response.json()

    def get_cities_with_content_on_requested_languages(self, languages=None):
        """
        Get list of cities that have content on requested languages.
        Args:
            languages (str): Requested languages.
        Returns:
            list: List of cities.
        """
        url = "{base_url}cities".format(base_url=self.api_url)
        if languages is None:
            params = self._prepare_params()
        else:
            params = self._prepare_params(languages=languages)
        response = requests.get(url, params, headers=self.headers)
        self._check_response_status(response)

        cities_data = response.json()
        cities = []
        if cities_data:
            for city in cities_data:

                city_title = city.get("title")
                city_uuid = city.get("uuid")
                cities.append({"city_title": city_title,
                               "city_uuid": city_uuid})
            return cities
        return cities


client = IziTravelClient()
print (client.find_city_by_name("Lviv"))
print client.get_city_museums("Lviv")
print client.get_city_tours("Lviv")
mus_uuid = client.get_city_museums("Lviv")[0]["museum_uuid"]
print client.get_museum_detail_with_audio(mus_uuid)
for key, value in client.get_museum_detail_with_audio(mus_uuid).items():
    print(key, value)
tour_id = client.get_city_tours("Lviv")[0]["uuid"]
print tour_id
print client.get_tourist_attractions(tour_id)
print client.get_object_reviews_and_rating(tour_id)
print client.get_featured_content()[0]
print client.get_cities_with_content_on_requested_languages("uk")
