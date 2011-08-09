
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVPortSetting(DynamicData):
    '''Network related configuration of a DistributedVirtualPort.
    '''
    
    def __init__(self, blocked, inShapingPolicy, outShapingPolicy, vendorSpecificConfig, vmDirectPathGen2Allowed):
        # MUST define these
        super(DVPortSetting, self).__init__()
    
        self.data['blocked'] = blocked
        self.data['inShapingPolicy'] = inShapingPolicy
        self.data['outShapingPolicy'] = outShapingPolicy
        self.data['vendorSpecificConfig'] = vendorSpecificConfig
        self.data['vmDirectPathGen2Allowed'] = vmDirectPathGen2Allowed
    
    
    @property
    def blocked(self):
        '''Whether this port is blocked, i.e. packet forwarding is stopped.
        '''
        return self.data['blocked']

    @property
    def inShapingPolicy(self):
        '''The network shaping policy for controlling in-throughput.
        '''
        return self.data['inShapingPolicy']

    @property
    def outShapingPolicy(self):
        '''The network shaping policy for controlling out-throughput.
        '''
        return self.data['outShapingPolicy']

    @property
    def vendorSpecificConfig(self):
        '''An opaque binary blob that stores vendor specific configuration.
        '''
        return self.data['vendorSpecificConfig']

    @property
    def vmDirectPathGen2Allowed(self):
        '''Whether this port is allowed to do VMDirectPath Gen2 network passthrough.
        '''
        return self.data['vmDirectPathGen2Allowed']

