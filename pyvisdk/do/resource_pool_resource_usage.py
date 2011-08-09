
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ResourcePoolResourceUsage(DynamicData):
    '''Specifies the resource usage for either memory or CPU. For CPU the unit is MHz,
        for memory the unit is bytes.In the typical case, where a resourcepool is
        in a consistent state, unreservedForVm will be equal to unreservedForPool.
        Hence, we can simply say talk about unreserved resources.If the
        reservation on the resource pool is not expandable, then the following is
        true:If the reservation on the resource pool is expandable, then the
        following is true:
    '''
    
    def __init__(self, maxUsage, overallUsage, reservationUsed, reservationUsedForVm, unreservedForPool, unreservedForVm):
        # MUST define these
        super(ResourcePoolResourceUsage, self).__init__()
    
        self.data['maxUsage'] = maxUsage
        self.data['overallUsage'] = overallUsage
        self.data['reservationUsed'] = reservationUsed
        self.data['reservationUsedForVm'] = reservationUsedForVm
        self.data['unreservedForPool'] = unreservedForPool
        self.data['unreservedForVm'] = unreservedForVm
    
    
    @property
    def maxUsage(self):
        '''Current upper-bound on usage. The upper-bound is based on the limit configured on
        this resource pool, as well as limits configured on any parent resource
        pool.
        '''
        return self.data['maxUsage']

    @property
    def overallUsage(self):
        '''Close to real-time resource usage of all running child virtual machines, including
        virtual machines in child resource pools.
        '''
        return self.data['overallUsage']

    @property
    def reservationUsed(self):
        '''Total amount of resources that have been used to satisfy the reservation
        requirements of all descendants of this resource pool (includes both
        resource pools and virtual machines).
        '''
        return self.data['reservationUsed']

    @property
    def reservationUsedForVm(self):
        '''Total amount of resources that have been used to satisfy the reservation
        requirements of running virtual machines in this resource pool or any of
        its child resource pools.
        '''
        return self.data['reservationUsedForVm']

    @property
    def unreservedForPool(self):
        '''Total amount of resources available to satisfy a reservation for a child resource
        pool. In the undercommitted state, this is limited by the capacity at the
        root node. In the overcommitted case, this could be higher since we do not
        perform the dynamic capacity checks.
        '''
        return self.data['unreservedForPool']

    @property
    def unreservedForVm(self):
        '''Total amount of resources available to satisfy a reservation for a child virtual
        machine. In general, this should be the same as unreservedForPool.
        However, in the overcommitted case, this is limited by the remaining
        available resources at the root node.
        '''
        return self.data['unreservedForVm']

