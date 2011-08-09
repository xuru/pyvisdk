
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostShortNameToIpFailedEvent(HostEvent):
    '''This event records that the host's short name could not be resolved to an IP
        address.
    '''
    
    def __init__(self, shortName):
        # MUST define these
        super(HostShortNameToIpFailedEvent, self).__init__()
    
        self.data['shortName'] = shortName
    
    
    @property
    def shortName(self):
        '''
        '''
        return self.data['shortName']

