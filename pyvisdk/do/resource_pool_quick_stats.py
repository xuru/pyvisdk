
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ResourcePoolQuickStats(DynamicData):
    '''A set of statistics that are typically updated with near real-time regularity.
        These statistics are aggregates of the corresponding statistics of all
        virtual machines in the given resource pool, and unless otherwise noted,
        only make sense when at least one virtual machine in the given resource
        pool is powered on. This data object type does not support notification,
        for scalability reasons. Therefore, changes in QuickStats do not generate
        property collector updates. To monitor statistics values, use the
        statistics and alarms modules instead.
    '''
    
    def __init__(self, balloonedMemory, compressedMemory, consumedOverheadMemory, distributedCpuEntitlement, distributedMemoryEntitlement, guestMemoryUsage, hostMemoryUsage, overallCpuDemand, overallCpuUsage, overheadMemory, privateMemory, sharedMemory, staticCpuEntitlement, staticMemoryEntitlement, swappedMemory):
        # MUST define these
        super(ResourcePoolQuickStats, self).__init__()
    
        self.data['balloonedMemory'] = balloonedMemory
        self.data['compressedMemory'] = compressedMemory
        self.data['consumedOverheadMemory'] = consumedOverheadMemory
        self.data['distributedCpuEntitlement'] = distributedCpuEntitlement
        self.data['distributedMemoryEntitlement'] = distributedMemoryEntitlement
        self.data['guestMemoryUsage'] = guestMemoryUsage
        self.data['hostMemoryUsage'] = hostMemoryUsage
        self.data['overallCpuDemand'] = overallCpuDemand
        self.data['overallCpuUsage'] = overallCpuUsage
        self.data['overheadMemory'] = overheadMemory
        self.data['privateMemory'] = privateMemory
        self.data['sharedMemory'] = sharedMemory
        self.data['staticCpuEntitlement'] = staticCpuEntitlement
        self.data['staticMemoryEntitlement'] = staticMemoryEntitlement
        self.data['swappedMemory'] = swappedMemory
    
    
    @property
    def balloonedMemory(self):
        '''The size of the balloon driver in a virtual machine, in MB. The host will inflate
        the balloon driver to reclaim physical memory from a virtual machine. This
        is a sign that there is memory pressure on the host.
        '''
        return self.data['balloonedMemory']

    @property
    def compressedMemory(self):
        '''The amount of compressed memory currently consumed by VM, in KB.
        '''
        return self.data['compressedMemory']

    @property
    def consumedOverheadMemory(self):
        '''The amount of overhead memory, in MB, currently being consumed to run a VM. This
        value is limited by the overhead memory reservation for a VM, stored in
        overheadMemory.
        '''
        return self.data['consumedOverheadMemory']

    @property
    def distributedCpuEntitlement(self):
        '''This is the amount of CPU resource, in MHz, that this VM is entitled to, as
        calculated by DRS. Valid only for a VM managed by DRS.
        '''
        return self.data['distributedCpuEntitlement']

    @property
    def distributedMemoryEntitlement(self):
        '''This is the amount of memory, in MB, that this VM is entitled to, as calculated by
        DRS. Valid only for a VM managed by DRS.
        '''
        return self.data['distributedMemoryEntitlement']

    @property
    def guestMemoryUsage(self):
        '''Guest memory utilization statistics, in MB. This is also known as active guest
        memory. The number can be between 0 and the configured memory size of a
        virtual machine.
        '''
        return self.data['guestMemoryUsage']

    @property
    def hostMemoryUsage(self):
        '''Host memory utilization statistics, in MB. This is also known as consummed host
        memory. This is between 0 and the configured resource limit. Valid while a
        virtual machine is running. This includes the overhead memory of a virtual
        machine.
        '''
        return self.data['hostMemoryUsage']

    @property
    def overallCpuDemand(self):
        '''Basic CPU performance statistics, in MHz.
        '''
        return self.data['overallCpuDemand']

    @property
    def overallCpuUsage(self):
        '''Basic CPU performance statistics, in MHz.
        '''
        return self.data['overallCpuUsage']

    @property
    def overheadMemory(self):
        '''The amount of memory resource (in MB) that will be used by a virtual machine above
        its guest memory requirements. This value is set if and only if a virtual
        machine is registered on a host that supports memory resource allocation
        features. For powered off VMs, this is the minimum overhead required to
        power on the VM on the registered host. For powered on VMs, this is the
        current overhead reservation, a value which is almost always larger than
        the minimum overhead, and which grows with time.
        '''
        return self.data['overheadMemory']

    @property
    def privateMemory(self):
        '''The portion of memory, in MB, that is granted to a virtual machine from non-shared
        host memory.
        '''
        return self.data['privateMemory']

    @property
    def sharedMemory(self):
        '''The portion of memory, in MB, that is granted to a virtual machine from host
        memory that is shared between VMs.
        '''
        return self.data['sharedMemory']

    @property
    def staticCpuEntitlement(self):
        '''The static CPU resource entitlement for a virtual machine. This value is
        calculated based on this virtual machine's resource reservations, shares
        and limit, and doesn't take into account current usage. This is the worst
        case CPU allocation for this virtual machine, that is, the amount of CPU
        resource this virtual machine would receive if all virtual machines
        running in the cluster went to maximum consumption. Units are MHz.
        '''
        return self.data['staticCpuEntitlement']

    @property
    def staticMemoryEntitlement(self):
        '''The static memory resource entitlement for a virtual machine. This value is
        calculated based on this virtual machine's resource reservations, shares
        and limit, and doesn't take into account current usage. This is the worst
        case memory allocation for this virtual machine, that is, the amount of
        memory this virtual machine would receive if all virtual machines running
        in the cluster went to maximum consumption. Units are MB.
        '''
        return self.data['staticMemoryEntitlement']

    @property
    def swappedMemory(self):
        '''The portion of memory, in MB, that is granted to a virtual machine from the host's
        swap space. This is a sign that there is memory pressure on the host.
        '''
        return self.data['swappedMemory']

