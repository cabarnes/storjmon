"""Storj API tests."""
from http import HTTPStatus
from unittest import TestCase

import responses

from common.storj import ApiException
from common.storj import StorjApi


class StorjTestCase(TestCase):
    """Storj API tests."""

    def setUp(self):
        """Test setup."""
        super().setUp()

        self.base_url = 'https://api.storj.io'
        self.node_id = '46e06e30f55c3aa7072a3a124ec2460fa23d4c9e'
        self.api = StorjApi()

    @responses.activate
    def test_get_contact_info(self):
        """Test getting contact info."""
        info = {
            'lastSeen': '2018-02-17T02:26:01.612Z',
            'port': 4000,
            'address': 'somedomain.com',
            'userAgent': '8.6.0',
            'protocol': '1.2.0',
            'responseTime': 7449.653797849757,
            'lastTimeout': '2018-01-02T21:42:47.158Z',
            'timeoutRate': 0,
            'spaceAvailable': True,
            'lastContractSent': 1507760610279,
            'reputation': 271,
            'nodeID': self.node_id,
        }
        responses.add(
            responses.GET,
            self.base_url + '/contacts/' + self.node_id,
            status=HTTPStatus.OK,
            json=info
        )

        result = self.api.get_contact_info(self.node_id)

        self.assertEqual(result, info)

    @responses.activate
    def test_get_contact_info_error(self):
        """Test getting contact info with an error."""
        responses.add(
            responses.GET,
            self.base_url + '/contacts/' + self.node_id,
            status=HTTPStatus.NOT_FOUND,
            json={'error': 'Contact not found'}
        )

        with self.assertRaises(ApiException) as exc:
            self.api.get_contact_info(self.node_id)

        self.assertEqual(exc.exception.status_code, HTTPStatus.NOT_FOUND)
        self.assertEqual(exc.exception.message, 'Contact not found')
