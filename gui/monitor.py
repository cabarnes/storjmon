"""Monitor a Storj node via web interface."""
from http import HTTPStatus

from flask import Flask
from flask import render_template
from flask_restful import Resource, Api

from common.aggregator import Aggregator
from common.storj import ApiException
from common.storj import StorjApi

app = Flask(__name__)
api = Api(app)
aggregator = Aggregator()


@app.route('/')
def home():
    """Home page."""
    return render_template('index.html')


class Contacts(Resource):
    """Contacts API."""

    @staticmethod
    def get(node_id):
        """GET handler."""
        storj_api = StorjApi()
        try:
            info = storj_api.get_contact_info(node_id)
            return info
        except ApiException as exception:
            return 'Error retrieving information: {}'.format(
                exception.message), exception.status_code


class Monitor(Resource):
    """Monitor API."""

    @staticmethod
    def post(node_id):
        """POST handler."""
        if aggregator.start(node_id):
            return '', HTTPStatus.CREATED

        return (
            'Unable to start monitoring {}'.format(node_id),
            HTTPStatus.BAD_REQUEST
        )

    @staticmethod
    def delete(node_id):
        """DELETE handler."""
        if aggregator.stop(node_id):
            return None, HTTPStatus.NO_CONTENT

        return (
            'Unable to stop monitoring {}'.format(node_id),
            HTTPStatus.BAD_REQUEST
        )


api.add_resource(
    Contacts,
    '/api/v1/contacts/<node_id>',
    endpoint='api.contacts'
)

api.add_resource(
    Monitor,
    '/api/v1/monitor/<node_id>',
    endpoint='api.monitor'
)

if __name__ == '__main__':  # pragma: no cover
    app.run(debug=True)
