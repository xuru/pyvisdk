
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostNetworkConfigResult(DynamicData):
    '''The result returned by updateNetworkConfig call. See UpdateNetworkConfig
    '''
    
    def __init__(self, consoleVnicDevice, vnicDevice):
        # MUST define these
        super(HostNetworkConfigResult, self).__init__()
    
        self.data['consoleVnicDevice'] = consoleVnicDevice
        self.data['vnicDevice'] = vnicDevice
    
    
    @property
    def consoleVnicDevice(self):
        '''Service console virtual network adapter keys.
        '''
        return self.data['consoleVnicDevice']

    @property
    def vnicDevice(self):
        '''Virtual network adapter keys.
        '''
        return self.data['vnicDevice']

