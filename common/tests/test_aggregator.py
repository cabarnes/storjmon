"""Aggregator tests."""
from http import HTTPStatus
from unittest import TestCase
from unittest.mock import MagicMock
from unittest.mock import patch

from apscheduler.schedulers.background import BackgroundScheduler

from common.aggregator import Aggregator
from common.storj import ApiException
from common.storj import StorjApi

# pylint: disable=protected-access


class AggregatorTestCase(TestCase):
    """Aggregator tests."""

    def setUp(self):
        """Test setup."""
        super().setUp()

        self.node_id = '46e06e30f55c3aa7072a3a124ec2460fa23d4c9e'
        self.aggregator = Aggregator()

    @patch.object(BackgroundScheduler, 'get_job')
    @patch.object(BackgroundScheduler, 'add_job')
    def test_start(self, mock_add_job, mock_get_job):
        """Test starting aggregation."""
        mock_get_job.return_value = None

        result = self.aggregator.start(self.node_id)

        self.assertTrue(result)
        self.assertTrue(mock_add_job.called)

    @patch.object(BackgroundScheduler, 'get_job')
    @patch.object(BackgroundScheduler, 'add_job')
    def test_start_already_running(self, mock_add_job, mock_get_job):
        """Test starting aggregation when already running."""
        mock_get_job.return_value = MagicMock()

        result = self.aggregator.start(self.node_id)

        self.assertFalse(result)
        self.assertFalse(mock_add_job.called)

    @patch.object(BackgroundScheduler, 'get_job')
    def test_stop(self, mock_get_job):
        """Test stopping aggregation."""
        mock_get_job.return_value = MagicMock()

        result = self.aggregator.stop(self.node_id)

        self.assertTrue(result)
        self.assertTrue(mock_get_job.return_value.remove.called)

    @patch.object(BackgroundScheduler, 'get_job')
    def test_stop_nothing(self, mock_get_job):
        """Test stopping aggregation with nothing running."""
        mock_get_job.return_value = None

        result = self.aggregator.stop(self.node_id)

        self.assertFalse(result)

    @patch.object(StorjApi, 'get_contact_info')
    def test_store_data(self, mock_contact):
        """Test storing data."""
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

        self.aggregator._store_data(self.node_id)

    @patch.object(StorjApi, 'get_contact_info')
    def test_store_data_api_error(self, mock_contact):
        """Test storing data with an API error."""
        message = b'Something went wrong. Our team has been notified.'
        mock_contact.side_effect = ApiException(
            HTTPStatus.INTERNAL_SERVER_ERROR,
            message
        )

        self.aggregator._store_data(self.node_id)
