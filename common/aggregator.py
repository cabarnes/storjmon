"""Store data over time from Storj."""
from apscheduler.schedulers.background import BackgroundScheduler

from .storj import ApiException
from .storj import StorjApi


class Aggregator(object):
    """Store data over time from Storj."""

    def __init__(self):
        self.api = StorjApi()
        self.scheduler = BackgroundScheduler()
        self.job = None

        self.scheduler.start()

    def _store_data(self, node_id):
        """Store the data for `node_id`."""
        try:
            info = self.api.get_contact_info(node_id)
            print(info)
        except ApiException as exception:
            print('Error retrieving information: {}'.format(exception.message))

    def start(self, node_id):
        """Start storing data."""
        if not self.job:
            self.job = self.scheduler.add_job(
                self._store_data, 'interval', seconds=1, args=[node_id])

    def stop(self):
        """Stop storing data."""
        if self.job:
            self.job.remove()
            self.job = None
