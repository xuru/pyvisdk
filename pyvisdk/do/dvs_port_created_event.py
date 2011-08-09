
from pyvisdk.do.dvs_event import DvsEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DvsPortCreatedEvent(DvsEvent):
    '''New ports are created in the distributed virtual switch.
    '''
    
    def __init__(self, portKey):
        # MUST define these
        super(DvsPortCreatedEvent, self).__init__()
    
        self.data['portKey'] = portKey
    
    
    @property
    def portKey(self):
        '''The key of the ports that are created.
        '''
        return self.data['portKey']

