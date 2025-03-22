from icmplib import ping
from netbox.jobs import JobRunner
from .utilities import ListHandler
import logging

__all__ = (
    'PingJob',
)

def get_job_log(job):
    job.data = {
        'log': []
    }
    return job.data['log']

class PingJob(JobRunner):
    '''
    ICMP Ping an IP and return some data about that.
    '''

    class Meta:
        name = 'Ping'

    def run(self, data, commit, *args, **kwargs):
        logger = logging.getLogger('netbox_dashy.ping')
        logger.setLevel(logging.DEBUG)
        logger.addHandler(ListHandler(queue=get_job_log(self.job)))

        try:
            results = ping(address=data['target'], count=data['count'], interval=data['interval'])
            return results
        except NameLookupError:
            return {'error': f'Failed to resolve {kwargs['target']}'}
        except SocketPermissionError, SocketAddressError, ICMPSocketError:
            return {'error': f'Failed to bind to socket.'}
        except Exception as e:
            logger.info("Failed to ping")