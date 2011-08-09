
from pyvisdk.do.virtual_device_device_backing_info import VirtualDeviceDeviceBackingInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualEthernetCardNetworkBackingInfo(VirtualDeviceDeviceBackingInfo):
    '''The virtual Ethernet card backing class.
    '''
    
    def __init__(self, inPassthroughMode, network):
        # MUST define these
        super(VirtualEthernetCardNetworkBackingInfo, self).__init__()
    
        self.data['inPassthroughMode'] = inPassthroughMode
        self.data['network'] = network
    
    
    @property
    def inPassthroughMode(self):
        '''deprecated As of vSphere API 4.0, this property is not supported.
        '''
        return self.data['inPassthroughMode']

    @property
    def network(self):
        '''Reference to the network managed object to which this backing applies. This is not
        used during configuration.
        '''
        return self.data['network']

