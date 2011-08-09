
from pyvisdk.do.dvs_event import DvsEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DvsCreatedEvent(DvsEvent):
    '''A distributed virtual switch was created.
    '''
    
    def __init__(self, parent):
        # MUST define these
        super(DvsCreatedEvent, self).__init__()
    
        self.data['parent'] = parent
    
    
    @property
    def parent(self):
        '''The folder where the DistributedVirtualSwitch is created.
        '''
        return self.data['parent']

