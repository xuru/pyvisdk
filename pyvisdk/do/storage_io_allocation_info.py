
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class StorageIOAllocationInfo(DynamicData):
    '''The IOAllocationInfo specifies the shares and the limit for storage I/O
        resource.The storage I/O resource is allocated to virtual machines based
        on their shares and limit. We do not support reservation for storage I/O
        resource. And we do not support storage I/O resource management on
        resource pools.Each virtual machine has one IOAllocationInfo object per
        virtual disk. For example, we can specify that a virtual machine has 500
        shares on the first virtual disk, 1000 shares on the second virtual disk,
        etc.
    '''
    
    def __init__(self, limit, shares):
        # MUST define these
        super(StorageIOAllocationInfo, self).__init__()
    
        self.data['limit'] = limit
        self.data['shares'] = shares
    
    
    @property
    def limit(self):
        '''The utilization of a virtual machine will not exceed this limit, even if there are
        available resources. This is typically used to ensure a consistent
        performance of virtual machines independent of available resources. If set
        to -1, then there is no fixed limit on resource usage (only bounded by
        available resources and shares). The unit is number of I/O per second.
        While setting the limit for storage I/O resource, if the property is
        unset, it is treated as no change and the property is not updated. While
        reading back the limit information of storage I/O resource, if the
        property is unset, a default value of -1 will be returned, which indicates
        that there is no limit on resource usage.
        '''
        return self.data['limit']

    @property
    def shares(self):
        '''Shares are used in case of resource contention. The value should be within a range
        of 200 to 4000. While setting shares for storage I/O resource, if the
        property is unset, it is treated as no change and the property is not
        updated. While reading back the shares information of storage I/O
        resource, if the property is unset, a default value of level = normal,
        shares = 1000 will be returned.
        '''
        return self.data['shares']

