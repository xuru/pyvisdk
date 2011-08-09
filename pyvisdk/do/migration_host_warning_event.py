
from pyvisdk.do.migration_event import MigrationEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class MigrationHostWarningEvent(MigrationEvent):
    '''A migration warning that includes the destination host.
    '''
    
    def __init__(self, dstHost):
        # MUST define these
        super(MigrationHostWarningEvent, self).__init__()
    
        self.data['dstHost'] = dstHost
    
    
    @property
    def dstHost(self):
        '''The name of the destination host.
        '''
        return self.data['dstHost']

