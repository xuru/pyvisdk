
from pyvisdk.do.dvs_event import DvsEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DvsReconfiguredEvent(DvsEvent):
    '''A distributed virtual switch was reconfigured.
    '''
    
    def __init__(self, configSpec):
        # MUST define these
        super(DvsReconfiguredEvent, self).__init__()
    
        self.data['configSpec'] = configSpec
    
    
    @property
    def configSpec(self):
        '''The reconfiguration spec.
        '''
        return self.data['configSpec']

