
from pyvisdk.do.dvs_event import DvsEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DvsHostBackInSyncEvent(DvsEvent):
    '''The DVS configuration on the host was synchronized with that of the Virtual Center
        Server and the configuration is the same on the host and Virtual Center
        Server.
    '''
    
    def __init__(self, hostBackInSync):
        # MUST define these
        super(DvsHostBackInSyncEvent, self).__init__()
    
        self.data['hostBackInSync'] = hostBackInSync
    
    
    @property
    def hostBackInSync(self):
        '''The host that was synchronized.
        '''
        return self.data['hostBackInSync']

