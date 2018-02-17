"""Interface to the Storj API."""
import requests

from urllib.parse import urljoin


class ApiException(Exception):
    """Exception contacting Storj API."""

    def __init__(self, status_code, message):
        self._status_code = status_code
        self._message = message

    @property
    def status_code(self):
        """Get the status code."""
        return self._status_code

    @property
    def message(self):
        """Get the message."""
        return self._message


class StorjApi(object):
    """Interface to the Storj API."""

    def __init__(self, base_url='https://api.storj.io'):
        self.base_url = base_url

    def get_contact_info(self, node_id):
        """Get the contact info for `node_id`."""
        response = requests.get(
            urljoin(self.base_url, '/contacts/{}'.format(node_id)))

        if response.status_code == 200:
            return response.json()
        else:
            raise ApiException(response.status_code, response.json()['error'])
