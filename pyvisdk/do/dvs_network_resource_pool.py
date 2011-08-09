
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVSNetworkResourcePool(DynamicData):
    '''DataObject describing the resource configuration and management of network
        resource pools.
    '''
    
    def __init__(self, allocationInfo, configVersion, description, key, name):
        # MUST define these
        super(DVSNetworkResourcePool, self).__init__()
    
        self.data['allocationInfo'] = allocationInfo
        self.data['configVersion'] = configVersion
        self.data['description'] = description
        self.data['key'] = key
        self.data['name'] = name
    
    
    @property
    def allocationInfo(self):
        '''The resource settings of the resource pool.
        '''
        return self.data['allocationInfo']

    @property
    def configVersion(self):
        '''The config version for the network resource pool.
        '''
        return self.data['configVersion']

    @property
    def description(self):
        '''The description of the network resource pool.
        '''
        return self.data['description']

    @property
    def key(self):
        '''The key of the network resource pool.
        '''
        return self.data['key']

    @property
    def name(self):
        '''The name of the network resource pool.
        '''
        return self.data['name']

