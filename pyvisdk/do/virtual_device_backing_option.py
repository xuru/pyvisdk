
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDeviceBackingOption(DynamicData):
    '''The VirtualDeviceBackingOption data class defines options for device-specific
        virtual backing objects.
    '''
    
    def __init__(self, type):
        # MUST define these
        super(VirtualDeviceBackingOption, self).__init__()
    
        self.data['type'] = type
    
    
    @property
    def type(self):
        '''The name of the class the client should use to instantiate backing for the virtual
        device.
        '''
        return self.data['type']

