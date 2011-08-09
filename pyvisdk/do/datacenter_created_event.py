
from pyvisdk.do.datacenter_event import DatacenterEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DatacenterCreatedEvent(DatacenterEvent):
    '''
    '''
    
    def __init__(self, parent):
        # MUST define these
        super(DatacenterCreatedEvent, self).__init__()
    
        self.data['parent'] = parent
    
    
    @property
    def parent(self):
        '''The folder where the datacenter is created.
        '''
        return self.data['parent']

