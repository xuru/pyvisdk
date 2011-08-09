
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ResourceAllocationInfo(DynamicData):
    '''The ResourceAllocationInfo data object specifies the reserved resource requirement
        as well as the limit (maximum allowed usage) for a given kind of resource.
        This is specified for both memory allocation (specified in MB) and CPU
        allocation (specified in MHz).For a ResourcePool, the
        ResourceAllocationInfo object describes both the guaranteed amount of the
        resource (reservation) and whether or not it is expandable
        (expandableReservation). If expandableReservation is true, then the
        resource pool can grow its reservation dynamically by borrowing unreserved
        resources from its parent resource pool. For the methods
        CreateResourcePool, CreateVApp and ImportVApp, you must provide values for
        all properties except overheadLimit; they are not optional. (Currently,
        overheadLimit is for VMware internal use only.)If the limit is configured,
        it must be greater than or equal to the reservation.
    '''
    
    def __init__(self, expandableReservation, limit, overheadLimit, reservation, shares):
        # MUST define these
        super(ResourceAllocationInfo, self).__init__()
    
        self.data['expandableReservation'] = expandableReservation
        self.data['limit'] = limit
        self.data['overheadLimit'] = overheadLimit
        self.data['reservation'] = reservation
        self.data['shares'] = shares
    
    
    @property
    def expandableReservation(self):
        '''In a resource pool with an expandable reservation, the reservation on a resource
        pool can grow beyond the specified value, if the parent resource pool has
        unreserved resources. A non-expandable reservation is called a fixed
        reservation. This property is ignored for virtual machines.
        '''
        return self.data['expandableReservation']

    @property
    def limit(self):
        '''The utilization of a virtual machine/resource pool will not exceed this limit,
        even if there are available resources. This is typically used to ensure a
        consistent performance of virtual machines / resource pools independent of
        available resources. If set to -1, then there is no fixed limit on
        resource usage (only bounded by available resources and shares). Units are
        MB for memory, MHz for CPU.
        '''
        return self.data['limit']

    @property
    def overheadLimit(self):
        '''The maximum allowed overhead memory. For a powered on virtual machine, the
        overhead memory reservation cannot be larger than its overheadLimit. This
        property is only applicable to powered on virtual machines and is not
        persisted across reboots. This property is not applicable for resource
        pools. If set to -1, then there is no limit on reservation. Units are MB.
        '''
        return self.data['overheadLimit']

    @property
    def reservation(self):
        '''Amount of resource that is guaranteed available to the virtual machine or resource
        pool. Reserved resources are not wasted if they are not used. If the
        utilization is less than the reservation, the resources can be utilized by
        other running virtual machines. Units are MB for memory, MHz for CPU.
        '''
        return self.data['reservation']

    @property
    def shares(self):
        '''Memory shares are used in case of resource contention.
        '''
        return self.data['shares']

