
from pyvisdk.do.dvs_event import DvsEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DvsHostLeftEvent(DvsEvent):
    '''A host left the distributed virtual switch.
    '''
    
    def __init__(self, hostLeft):
        # MUST define these
        super(DvsHostLeftEvent, self).__init__()
    
        self.data['hostLeft'] = hostLeft
    
    
    @property
    def hostLeft(self):
        '''The host that left DVS.
        '''
        return self.data['hostLeft']

