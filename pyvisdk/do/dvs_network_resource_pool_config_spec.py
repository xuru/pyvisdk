
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVSNetworkResourcePoolConfigSpec(DynamicData):
    '''The configuration specification data object to update the resource configuration
        for a network resource pool.
    '''
    
    def __init__(self, allocationInfo, configVersion, key):
        # MUST define these
        super(DVSNetworkResourcePoolConfigSpec, self).__init__()
    
        self.data['allocationInfo'] = allocationInfo
        self.data['configVersion'] = configVersion
        self.data['key'] = key
    
    
    @property
    def allocationInfo(self):
        '''The network resource allocation for the network resource pool.
        '''
        return self.data['allocationInfo']

    @property
    def configVersion(self):
        '''The configVersion is a unique identifier for a given version of the configuration.
        Each change to the configuration will update this value. This is typically
        implemented as a non-decreasing count or a time-stamp. However, a client
        should always treat this as an opaque string.
        '''
        return self.data['configVersion']

    @property
    def key(self):
        '''The key of the network resource pool.
        '''
        return self.data['key']

