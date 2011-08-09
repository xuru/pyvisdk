
from pyvisdk.do.dvs_event import DvsEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class OutOfSyncDvsHost(DvsEvent):
    '''The list of hosts that have the DVS configuration on the host diverged from that
        of the Virtual Center Server.
    '''
    
    def __init__(self, hostOutOfSync):
        # MUST define these
        super(OutOfSyncDvsHost, self).__init__()
    
        self.data['hostOutOfSync'] = hostOutOfSync
    
    
    @property
    def hostOutOfSync(self):
        '''The host that went out of sync.
        '''
        return self.data['hostOutOfSync']

