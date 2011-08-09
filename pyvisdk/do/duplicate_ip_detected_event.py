
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DuplicateIpDetectedEvent(HostEvent):
    '''This event records that a duplicate IP address has been observed in conflict with
        the vmotion or IP storage interface configured on the host.
    '''
    
    def __init__(self, duplicateIP, macAddress):
        # MUST define these
        super(DuplicateIpDetectedEvent, self).__init__()
    
        self.data['duplicateIP'] = duplicateIP
        self.data['macAddress'] = macAddress
    
    
    @property
    def duplicateIP(self):
        '''The Duplicate IP address detected.
        '''
        return self.data['duplicateIP']

    @property
    def macAddress(self):
        '''The MAC associated with duplicate IP.
        '''
        return self.data['macAddress']

