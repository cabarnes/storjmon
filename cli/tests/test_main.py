"""Main tests."""
from http import HTTPStatus
from unittest import TestCase
from unittest.mock import patch

from cli.__main__ import main
from common.storj import ApiException
from common.storj import StorjApi


class MainTestCase(TestCase):
    """Main tests."""

    def setUp(self):
        """Test setup."""
        super().setUp()

        self.node_id = '46e06e30f55c3aa7072a3a124ec2460fa23d4c9e'
        self.info = {
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

    @patch('builtins.print')
    @patch('cli.__main__.docopt')
    @patch.object(StorjApi, 'get_contact_info')
    def test_printing_info(self, mock_contact, mock_docopt, mock_print):
        """Test printing info for a node."""
        mock_contact.return_value = self.info
        mock_docopt.return_value = {
            '<node_id>': self.node_id,
            '--url': [],
        }

        main()

        self.assertTrue(mock_contact.called)
        self.assertEqual(mock_contact.call_args[0][0], self.node_id)
        self.assertEqual(mock_print.call_count, len(self.info))

    @patch('builtins.print')
    @patch('cli.__main__.docopt')
    @patch.object(StorjApi, 'get_contact_info')
    def test_printing_info_custom_url(self, mock_contact, mock_docopt,
                                      mock_print):
        """Test printing info for a node with a custom URL."""
        mock_contact.return_value = self.info
        mock_docopt.return_value = {
            '<node_id>': self.node_id,
            '--url': ['https://api.example.com'],
        }

        main()

        self.assertTrue(mock_contact.called)
        self.assertEqual(mock_contact.call_args[0][0], self.node_id)
        self.assertEqual(mock_print.call_count, len(self.info))

    @patch('builtins.print')
    @patch('cli.__main__.docopt')
    @patch.object(StorjApi, 'get_contact_info')
    def test_printing_info_api_error(self, mock_contact, mock_docopt,
                                     mock_print):
        """Test printing info for a node with an API error."""
        message = 'Something went wrong. Our team has been notified.'
        mock_contact.side_effect = ApiException(
            HTTPStatus.INTERNAL_SERVER_ERROR,
            message
        )
        mock_docopt.return_value = {
            '<node_id>': self.node_id,
            '--url': [],
        }

        main()

        self.assertTrue(mock_contact.called)
        self.assertEqual(mock_contact.call_args[0][0], self.node_id)
        self.assertIn(message, mock_print.call_args[0][0])
