
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostAddFailedEvent(HostEvent):
    '''This event records that adding a host failed.
    '''
    
    def __init__(self, hostname):
        # MUST define these
        super(HostAddFailedEvent, self).__init__()
    
        self.data['hostname'] = hostname
    
    
    @property
    def hostname(self):
        '''
        '''
        return self.data['hostname']

