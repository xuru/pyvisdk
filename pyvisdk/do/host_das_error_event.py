
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDasErrorEvent(HostEvent):
    '''This event records when there is a HA error on a host.
    '''
    
    def __init__(self, message, reason):
        # MUST define these
        super(HostDasErrorEvent, self).__init__()
    
        self.data['message'] = message
        self.data['reason'] = reason
    
    
    @property
    def message(self):
        '''VI API 2.5
        '''
        return self.data['message']

    @property
    def reason(self):
        '''The reason for the failure.
        '''
        return self.data['reason']

