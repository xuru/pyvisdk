
from pyvisdk.do.dvs_event import DvsEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DvsPortEnteredPassthruEvent(DvsEvent):
    '''A port has entered passthrough mode on the distributed virtual switch.
    '''
    
    def __init__(self, portKey):
        # MUST define these
        super(DvsPortEnteredPassthruEvent, self).__init__()
    
        self.data['portKey'] = portKey
    
    
    @property
    def portKey(self):
        '''The port key.
        '''
        return self.data['portKey']

