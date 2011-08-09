
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineQuickStats(DynamicData):
    '''A set of statistics that are typically updated with near real-time regularity.
        This data object type does not support notification, for scalability
        reasons. Therefore, changes in QuickStats do not generate property
        collector updates. To monitor statistics values, use the statistics and
        alarms modules instead.
    '''
    
    def __init__(self, balloonedMemory, compressedMemory, consumedOverheadMemory, distributedCpuEntitlement, distributedMemoryEntitlement, ftLatencyStatus, ftLogBandwidth, ftSecondaryLatency, guestHeartbeatStatus, guestMemoryUsage, hostMemoryUsage, overallCpuDemand, overallCpuUsage, privateMemory, sharedMemory, staticCpuEntitlement, staticMemoryEntitlement, swappedMemory, uptimeSeconds):
        # MUST define these
        super(VirtualMachineQuickStats, self).__init__()
    
        self.data['balloonedMemory'] = balloonedMemory
        self.data['compressedMemory'] = compressedMemory
        self.data['consumedOverheadMemory'] = consumedOverheadMemory
        self.data['distributedCpuEntitlement'] = distributedCpuEntitlement
        self.data['distributedMemoryEntitlement'] = distributedMemoryEntitlement
        self.data['ftLatencyStatus'] = ftLatencyStatus
        self.data['ftLogBandwidth'] = ftLogBandwidth
        self.data['ftSecondaryLatency'] = ftSecondaryLatency
        self.data['guestHeartbeatStatus'] = guestHeartbeatStatus
        self.data['guestMemoryUsage'] = guestMemoryUsage
        self.data['hostMemoryUsage'] = hostMemoryUsage
        self.data['overallCpuDemand'] = overallCpuDemand
        self.data['overallCpuUsage'] = overallCpuUsage
        self.data['privateMemory'] = privateMemory
        self.data['sharedMemory'] = sharedMemory
        self.data['staticCpuEntitlement'] = staticCpuEntitlement
        self.data['staticMemoryEntitlement'] = staticMemoryEntitlement
        self.data['swappedMemory'] = swappedMemory
        self.data['uptimeSeconds'] = uptimeSeconds
    
    
    @property
    def balloonedMemory(self):
        '''The size of the balloon driver in the VM, in MB. The host will inflate the balloon
        driver to reclaim physical memory from the VM. This is a sign that there
        is memory pressure on the host.
        '''
        return self.data['balloonedMemory']

    @property
    def compressedMemory(self):
        '''The amount of compressed memory currently consumed by VM, in Kb.
        '''
        return self.data['compressedMemory']

    @property
    def consumedOverheadMemory(self):
        '''The amount of consumed overhead memory, in MB, for this VM.
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
    def ftLatencyStatus(self):
        '''The latency status of the fault tolerance VM. ftLatencyStatus is determined by the
        value of ftSecondaryLatency. ftLatencyStatus is: green, if
        ftSecondaryLatency is less than or equal to 2 seconds; yellow, if
        ftSecondaryLatency is greater than 2 seconds, and less than or equal to 6
        seconds; red, if ftSecondaryLatency is greater than 6 seconds; gray, if
        ftSecondaryLatency is unknown.
        '''
        return self.data['ftLatencyStatus']

    @property
    def ftLogBandwidth(self):
        '''The network bandwidth used for logging between the primary and secondary fault
        tolerance VMs. The unit is kilobytes per second.
        '''
        return self.data['ftLogBandwidth']

    @property
    def ftSecondaryLatency(self):
        '''The amount of time in wallclock that the VCPU of the secondary fault tolerance VM
        is behind the VCPU of the primary VM. The unit is millisecond.
        '''
        return self.data['ftSecondaryLatency']

    @property
    def guestHeartbeatStatus(self):
        '''Guest operating system heartbeat metric. See guestHeartbeatStatus for a
        description.
        '''
        return self.data['guestHeartbeatStatus']

    @property
    def guestMemoryUsage(self):
        '''Guest memory utilization statistics, in MB. This is also known as active guest
        memory. The number can be between 0 and the configured memory size of the
        virtual machine. Valid while the virtual machine is running.
        '''
        return self.data['guestMemoryUsage']

    @property
    def hostMemoryUsage(self):
        '''Host memory utilization statistics, in MB. This is also known as consumed host
        memory. This is between 0 and the configured resource limit. Valid while
        the virtual machine is running. This includes the overhead memory of the
        VM.
        '''
        return self.data['hostMemoryUsage']

    @property
    def overallCpuDemand(self):
        '''Basic CPU performance statistics, in MHz. Valid while the virtual machine is
        running.
        '''
        return self.data['overallCpuDemand']

    @property
    def overallCpuUsage(self):
        '''Basic CPU performance statistics, in MHz. Valid while the virtual machine is
        running.
        '''
        return self.data['overallCpuUsage']

    @property
    def privateMemory(self):
        '''The portion of memory, in MB, that is granted to this VM from non-shared host
        memory.
        '''
        return self.data['privateMemory']

    @property
    def sharedMemory(self):
        '''The portion of memory, in MB, that is granted to this VM from host memory that is
        shared between VMs.
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
        '''The portion of memory, in MB, that is granted to this VM from the host's swap
        space. This is a sign that there is memory pressure on the host.
        '''
        return self.data['swappedMemory']

    @property
    def uptimeSeconds(self):
        '''The system uptime of the VM in seconds.
        '''
        return self.data['uptimeSeconds']

