"""GUI tests."""
from http import HTTPStatus
from unittest import TestCase
from unittest.mock import patch

from flask import url_for
from pytest import fixture
from pytest import mark

from common.aggregator import Aggregator
from common.storj import ApiException
from common.storj import StorjApi
from gui.monitor import app as flask_app


@fixture
def app():
    """Create the test application."""
    return flask_app


class BaseTestCase(TestCase):
    """Base class for all test cases."""

    def setUp(self):
        """Test setup."""
        super().setUp()

        self.node_id = '46e06e30f55c3aa7072a3a124ec2460fa23d4c9e'


@mark.usefixtures('client_class')
class HomeTestCase(BaseTestCase):
    """Home page test case."""

    def test_home(self):
        """Test that the home page renders."""
        response = self.client.get(url_for('home'))

        self.assertEqual(response.status_code, HTTPStatus.OK)


@mark.usefixtures('client_class')
class ContactsTestCase(BaseTestCase):
    """Contacts API test case."""

    @patch.object(StorjApi, 'get_contact_info')
    def test_contacts(self, mock_contact):
        """Test contacts API returns node info."""
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
        mock_contact.return_value = info

        response = self.client.get(
            url_for('api.contacts', node_id=self.node_id))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertDictEqual(response.json, info)

    @patch.object(StorjApi, 'get_contact_info')
    def test_contacts_error(self, mock_contact):
        """Test contacts API returns error."""
        message = b'Something went wrong. Our team has been notified.'
        mock_contact.side_effect = ApiException(
            HTTPStatus.INTERNAL_SERVER_ERROR,
            message
        )

        response = self.client.get(
            url_for('api.contacts', node_id=self.node_id))

        self.assertEqual(
            response.status_code,
            HTTPStatus.INTERNAL_SERVER_ERROR
        )
        self.assertIn(message, response.data)


@mark.usefixtures('client_class')
class MonitorTestCase(BaseTestCase):
    """Monitor API test case."""

    @patch.object(Aggregator, 'start')
    def test_monitor_start(self, mock_start):
        """Test that the aggregator starts."""
        mock_start.return_value = True

        response = self.client.post(
            url_for('api.monitor', node_id=self.node_id))

        self.assertEqual(response.status_code, HTTPStatus.CREATED)

    @patch.object(Aggregator, 'start')
    def test_monitor_start_already_running(self, mock_start):
        """Test that the aggregator starts."""
        mock_start.return_value = False

        response = self.client.post(
            url_for('api.monitor', node_id=self.node_id))

        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    @patch.object(Aggregator, 'stop')
    def test_monitor_stop(self, mock_stop):
        """Test that the aggregator stops."""
        mock_stop.return_value = True

        response = self.client.delete(
            url_for('api.monitor', node_id=self.node_id))

        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)

    @patch.object(Aggregator, 'stop')
    def test_monitor_stop_not_running(self, mock_stop):
        """Test that the aggregator stops."""
        mock_stop.return_value = False

        response = self.client.delete(
            url_for('api.monitor', node_id=self.node_id))

        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
