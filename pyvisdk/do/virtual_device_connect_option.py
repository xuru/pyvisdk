
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDeviceConnectOption(DynamicData):
    '''The ConnectOption data object type contains information about options for
        connectable virtual devices.
    '''
    
    def __init__(self, allowGuestControl, startConnected):
        # MUST define these
        super(VirtualDeviceConnectOption, self).__init__()
    
        self.data['allowGuestControl'] = allowGuestControl
        self.data['startConnected'] = startConnected
    
    
    @property
    def allowGuestControl(self):
        '''Flag to indicate whether or not the device can be connected and disconnected from
        within the guest operating system.
        '''
        return self.data['allowGuestControl']

    @property
    def startConnected(self):
        '''Flag to indicate whether or not the device supports the startConnected feature.
        '''
        return self.data['startConnected']

