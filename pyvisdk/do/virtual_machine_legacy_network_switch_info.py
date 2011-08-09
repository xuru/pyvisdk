
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineLegacyNetworkSwitchInfo(DynamicData):
    '''The LegacyNetworkSwitchInfo data object type contains information about the legacy
        network switches available on the host.* VMware Server - Options available
        for the "custom" NetworkBackingType. * ESX Server - The "esxnet"
        NetworkBackingType.
    '''
    
    def __init__(self, name):
        # MUST define these
        super(VirtualMachineLegacyNetworkSwitchInfo, self).__init__()
    
        self.data['name'] = name
    
    
    @property
    def name(self):
        '''The name of the network switch.
        '''
        return self.data['name']

