
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDeviceConnectInfo(DynamicData):
    '''The data object type contains information about connectable virtual devices.
    '''
    
    def __init__(self, allowGuestControl, connected, startConnected, status):
        # MUST define these
        super(VirtualDeviceConnectInfo, self).__init__()
    
        self.data['allowGuestControl'] = allowGuestControl
        self.data['connected'] = connected
        self.data['startConnected'] = startConnected
        self.data['status'] = status
    
    
    @property
    def allowGuestControl(self):
        '''Enables guest control over whether the connectable device is connected.
        '''
        return self.data['allowGuestControl']

    @property
    def connected(self):
        '''Indicates whether the device is currently connected. Valid only while the virtual
        machine is running.
        '''
        return self.data['connected']

    @property
    def startConnected(self):
        '''Specifies whether or not to connect the device when the virtual machine starts.
        '''
        return self.data['startConnected']

    @property
    def status(self):
        '''Indicates the current status of the connectable device. Valid only while the
        virtual machine is running. The set of possible values is described in
        VirtualDeviceConnectInfoStatus
        '''
        return self.data['status']

