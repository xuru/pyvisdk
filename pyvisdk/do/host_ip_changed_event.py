
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostIpChangedEvent(HostEvent):
    '''This event records a change in host IP address.
    '''
    
    def __init__(self, newIP, oldIP):
        # MUST define these
        super(HostIpChangedEvent, self).__init__()
    
        self.data['newIP'] = newIP
        self.data['oldIP'] = oldIP
    
    
    @property
    def newIP(self):
        '''New IP address of the host.
        '''
        return self.data['newIP']

    @property
    def oldIP(self):
        '''Old IP address of the host.
        '''
        return self.data['oldIP']

