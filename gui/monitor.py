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
    return render_template('index.html')


class Contacts(Resource):
    def get(self, node_id):
        api = StorjApi()
        try:
            info = api.get_contact_info(node_id)
            return info
        except ApiException as exception:
            return 'Error retrieving information: {}'.format(
                exception.message), HTTPStatus.BAD_REQUEST


class Monitor(Resource):
    def post(self, node_id):
        aggregator.start(node_id)
        return '', HTTPStatus.CREATED

    def delete(self, node_id):
        aggregator.stop()
        return None, HTTPStatus.NO_CONTENT


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

if __name__ == '__main__':
    app.run(debug=True)
