
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVPortState(DynamicData):
    '''The state of a DistributedVirtualPort.
    '''
    
    def __init__(self, runtimeInfo, stats, vendorSpecificState):
        # MUST define these
        super(DVPortState, self).__init__()
    
        self.data['runtimeInfo'] = runtimeInfo
        self.data['stats'] = stats
        self.data['vendorSpecificState'] = vendorSpecificState
    
    
    @property
    def runtimeInfo(self):
        '''The run time information of the port. This property is set only when the port is
        running.
        '''
        return self.data['runtimeInfo']

    @property
    def stats(self):
        '''Statistics of the port.
        '''
        return self.data['stats']

    @property
    def vendorSpecificState(self):
        '''An opaque binary blob that stores vendor specific runtime state data.
        '''
        return self.data['vendorSpecificState']

