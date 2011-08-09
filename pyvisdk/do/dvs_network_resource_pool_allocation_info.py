
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVSNetworkResourcePoolAllocationInfo(DynamicData):
    '''Resource allocation information for a network resource pool.
    '''
    
    def __init__(self, limit, shares):
        # MUST define these
        super(DVSNetworkResourcePoolAllocationInfo, self).__init__()
    
        self.data['limit'] = limit
        self.data['shares'] = shares
    
    
    @property
    def limit(self):
        '''The maximum allowed usage for network clients belonging to this resource pool per
        host. The utilization of network clients belonging to this resource pool
        will not exceed the specified limit even if there are available network
        resources. If set to -1, then there is no limit on the network resource
        usage for clients belonging to this resource pool. Units are in Mbits/sec.
        When setting the allocation of a particular resource pool, if the property
        is unset, it is treated as no change and the property is not updated. An
        unset limit value while reading back the allocation information of a
        network resource pool indicates that there is no limit on the network
        resource usage for the clients belonging to this resource group.
        '''
        return self.data['limit']

    @property
    def shares(self):
        '''The share settings associated with the network resource pool to facilitate
        proportional sharing of the physical network resources. If the property is
        unset when setting the allocation of a particular resource pool, it is
        treated as unset and the property is not updated. The property is always
        set when reading back the allocation information of a network resource
        pool.
        '''
        return self.data['shares']

