
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineDeviceRuntimeInfo(DynamicData):
    '''The DeviceRuntimeInfo data object type provides information about the execution
        state of a single virtual device.
    '''
    
    def __init__(self, key, runtimeState):
        # MUST define these
        super(VirtualMachineDeviceRuntimeInfo, self).__init__()
    
        self.data['key'] = key
        self.data['runtimeState'] = runtimeState
    
    
    @property
    def key(self):
        '''The device key.
        '''
        return self.data['key']

    @property
    def runtimeState(self):
        '''The device runtime state.
        '''
        return self.data['runtimeState']

