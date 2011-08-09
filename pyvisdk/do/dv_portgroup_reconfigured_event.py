
from pyvisdk.do.dv_portgroup_event import DVPortgroupEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVPortgroupReconfiguredEvent(DVPortgroupEvent):
    '''Two distributed virtual portgroup was reconfigured.
    '''
    
    def __init__(self, configSpec):
        # MUST define these
        super(DVPortgroupReconfiguredEvent, self).__init__()
    
        self.data['configSpec'] = configSpec
    
    
    @property
    def configSpec(self):
        '''The reconfiguration spec.
        '''
        return self.data['configSpec']

