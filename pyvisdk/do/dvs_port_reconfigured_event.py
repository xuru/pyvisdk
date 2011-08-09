
from pyvisdk.do.dvs_event import DvsEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DvsPortReconfiguredEvent(DvsEvent):
    '''Existing ports are reconfigured in the distributed virtual switch.
    '''
    
    def __init__(self, portKey):
        # MUST define these
        super(DvsPortReconfiguredEvent, self).__init__()
    
        self.data['portKey'] = portKey
    
    
    @property
    def portKey(self):
        '''The key of the ports that are reconfigured.
        '''
        return self.data['portKey']

