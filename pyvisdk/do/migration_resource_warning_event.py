
from pyvisdk.do.migration_event import MigrationEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class MigrationResourceWarningEvent(MigrationEvent):
    '''A migration warning that includes both the destination host and resource pool.
    '''
    
    def __init__(self, dstHost, dstPool):
        # MUST define these
        super(MigrationResourceWarningEvent, self).__init__()
    
        self.data['dstHost'] = dstHost
        self.data['dstPool'] = dstPool
    
    
    @property
    def dstHost(self):
        '''The name of the destination host.
        '''
        return self.data['dstHost']

    @property
    def dstPool(self):
        '''The name of the destination resource pool.
        '''
        return self.data['dstPool']

