import allure
import curlify
import requests
from jsonschema import validate, ValidationError, SchemaError


class BaseAPI:
    def __init__(self, base_url, headers=None):
        """
        Initializes the BaseAPI class.

        :param base_url: The base URL of the API.
        :param headers: Dictionary of HTTP headers.
        """
        self.base_url = base_url
        self.headers = headers if headers else {}

    def attach_allure_info(self, response):
        allure.attach(curlify.to_curl(response.request), name="CURL", attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text, name="Response", attachment_type=allure.attachment_type.JSON)
        allure.attach(str(response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)

    def get(self, endpoint, params=None, headers=None, return_raw=False):
        """
        Performs a GET request.

        :param endpoint: The API endpoint.
        :param params: Query parameters.
        :param headers: Dictionary of HTTP headers.
        :param return_raw: If True, returns the raw response; otherwise, returns JSON.
        :return: JSON response or raw response.
        """
        response = requests.get(
            url=f"{self.base_url}/{endpoint}",
            params=params,
            headers=headers if headers else self.headers
        )
        return response if return_raw else response.json()

    def post(self, endpoint, data=None, json=None, headers=None, return_raw=False):
        """
        Performs a POST request.

        :param endpoint: The API endpoint.
        :param data: Data to send in the request body.
        :param json: JSON to send in the request body.
        :param headers: Dictionary of HTTP headers.
        :param return_raw: If True, returns the raw response; otherwise, returns JSON.
        :return: JSON response or raw response.
        """
        response = requests.post(
            url=f"{self.base_url}/{endpoint}",
            data=data,
            json=json,
            headers=headers if headers else self.headers
        )
        return response if return_raw else response.json()

    def put(self, endpoint, data=None, json=None, headers=None, return_raw=False):
        """
        Performs a PUT request.

        :param endpoint: The API endpoint.
        :param data: Data to send in the request body.
        :param json: JSON to send in the request body.
        :param headers: Dictionary of HTTP headers.
        :param return_raw: If True, returns the raw response; otherwise, returns JSON.
        :return: JSON response or raw response.
        """
        response = requests.put(
            url=f"{self.base_url}/{endpoint}",
            data=data,
            json=json,
            headers=headers if headers else self.headers
        )
        return response if return_raw else response.json()

    def delete(self, endpoint, headers=None, return_raw=False):
        """
        Performs a DELETE request.

        :param endpoint: The API endpoint.
        :param headers: Dictionary of HTTP headers.
        :param return_raw: If True, returns the raw response; otherwise, returns JSON.
        :return: JSON response or raw response.
        """
        response = requests.delete(
            url=f"{self.base_url}/{endpoint}",
            headers=headers if headers else self.headers
        )
        return response if return_raw else response.json()

    def validate_schema(self, schema, data):
        """
        Validates a dictionary against a provided JSON schema.

        :param schema: The JSON schema to validate against.
        :param data: The dictionary data to validate.
        :return: True if valid, raises ValidationError or SchemaError if invalid.
        """
        try:
            validate(instance=data, schema=schema)
            return True
        except ValidationError as ve:
            print(f"Validation error: {ve.message}")
            raise
        except SchemaError as se:
            print(f"Schema error: {se.message}")
            raise
