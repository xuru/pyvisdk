
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostCnxFailedAlreadyManagedEvent(HostEvent):
    '''This event records a failure to connect to a host due to the host being managed by
        a different VirtualCenter server.
    '''
    
    def __init__(self, serverName):
        # MUST define these
        super(HostCnxFailedAlreadyManagedEvent, self).__init__()
    
        self.data['serverName'] = serverName
    
    
    @property
    def serverName(self):
        '''The name of the VirtualCenter server that manages the host.
        '''
        return self.data['serverName']

