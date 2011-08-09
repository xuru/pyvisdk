
from pyvisdk.do.host_das_event import HostDasEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostIsolationIpPingFailedEvent(HostDasEvent):
    '''This event records that the isolation address could not be pinged. The default
        isolation address is the service console's default gateway.
    '''
    
    def __init__(self, isolationIp):
        # MUST define these
        super(HostIsolationIpPingFailedEvent, self).__init__()
    
        self.data['isolationIp'] = isolationIp
    
    
    @property
    def isolationIp(self):
        '''
        '''
        return self.data['isolationIp']

