"""Store data over time from Storj."""
from apscheduler.schedulers.background import BackgroundScheduler

from .storj import ApiException
from .storj import StorjApi


class Aggregator(object):
    """Store data over time from Storj."""

    def __init__(self):
        """Constructor."""
        self.api = StorjApi()
        self.scheduler = BackgroundScheduler()

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
        if not self.scheduler.get_job(job_id=node_id):
            self.scheduler.add_job(
                func=self._store_data,
                trigger='interval',
                id=node_id,
                seconds=1,
                args=[node_id]
            )
            return True

        return False

    def stop(self, node_id):
        """Stop storing data."""
        job = self.scheduler.get_job(job_id=node_id)
        if job:
            job.remove()
            return True

        return False
