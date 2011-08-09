
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualSwitchManagerDvsProductSpec(DynamicData):
    '''This class is used to specify ProductSpec for the DVS. The two properties are
        strictly mutually exclusive. If both properties are set, then an
        InvalidArgument fault would be thrown.
    '''
    
    def __init__(self, distributedVirtualSwitch, newSwitchProductSpec):
        # MUST define these
        super(DistributedVirtualSwitchManagerDvsProductSpec, self).__init__()
    
        self.data['distributedVirtualSwitch'] = distributedVirtualSwitch
        self.data['newSwitchProductSpec'] = newSwitchProductSpec
    
    
    @property
    def distributedVirtualSwitch(self):
        '''Get ProductSpec from the existing DVS
        '''
        return self.data['distributedVirtualSwitch']

    @property
    def newSwitchProductSpec(self):
        '''The ProductSpec for new DVS
        '''
        return self.data['newSwitchProductSpec']

