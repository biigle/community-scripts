import copy
import requests
from requests.auth import HTTPBasicAuth

class Api(object):
   def __init__(self, email, token, base_url = 'https://biigle.de/api/v1', headers = {}):
      """Create a new instance.

      Args:
         email (str): The email address of the user.
         token (str): The API token of the user.

      Kwargs:
         base_url (str): Base URL to use for the API URL. Default: `'https://biigle.de/api/v1'`.
         headers (dict): Default headers to use for each request. Default: `{'Accept': 'application/json'}`.
      """
      self.auth = HTTPBasicAuth(email, token)
      self.base_url = base_url
      self.headers = {'Accept': 'application/json'}
      self.headers.update(headers)

   def call(self, method, url, *args, **kwargs):
      """Perform an API call

      In addition to the method and URL, any args or kwargs of the requests method are
      accepted.

      Args:
         method: The requests method to use for the api call.
         url: The API endpoint to call.
      """
      if 'headers' in kwargs:
         headers = copy.deepcopy(self.headers)
         headers.update(kwargs['headers'])
      else:
         headers = self.headers
      kwargs['headers'] = headers
      kwargs['auth'] = self.auth

      response = method('{}/{}'.format(self.base_url, url), *args, **kwargs)
      response.raise_for_status()

      return response

   def get(self, url, *args, **kwargs):
      """Perform a GET request to the API

      See the `call` method for avaolable arguments.
      """
      return self.call(requests.get, url, *args, **kwargs)

   def post(self, url, *args, **kwargs):
      """Perform a POST request to the API

      See the `call` method for avaolable arguments.
      """
      return self.call(requests.post, url, *args, **kwargs)

   def put(self, url, *args, **kwargs):
      """Perform a PUT request to the API

      See the `call` method for avaolable arguments.
      """
      return self.call(requests.put, url, *args, **kwargs)

   def delete(self, url, *args, **kwargs):
      """Perform a DELETE request to the API

      See the `call` method for avaolable arguments.
      """
      return self.call(requests.delete, url, *args, **kwargs)

