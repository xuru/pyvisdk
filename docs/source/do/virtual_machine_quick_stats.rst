
================================================================================
VirtualMachineQuickStats
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_machine_summary.VirtualMachineSummary`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.managed_entity_status.ManagedEntityStatus`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.virtual_machine_quick_stats.VirtualMachineQuickStats
    
    .. py:attribute:: balloonedMemory
    
        The size of the balloon driver in the VM, in MB. The host will inflate the balloon driver to reclaim physical memory from the VM. This is a sign that there is memory pressure on the host.
        
    
    .. py:attribute:: compressedMemory
    
        The amount of compressed memory currently consumed by VM, in Kb.
        
    
    .. py:attribute:: consumedOverheadMemory
    
        The amount of consumed overhead memory, in MB, for this VM.
        
    
    .. py:attribute:: distributedCpuEntitlement
    
        This is the amount of CPU resource, in MHz, that this VM is entitled to, as calculated by DRS. Valid only for a VM managed by DRS.
        
    
    .. py:attribute:: distributedMemoryEntitlement
    
        This is the amount of memory, in MB, that this VM is entitled to, as calculated by DRS. Valid only for a VM managed by DRS.
        
    
    .. py:attribute:: ftLatencyStatus
    
        The latency status of the fault tolerance VM. ftLatencyStatus is determined by the value of ftSecondaryLatency. ftLatencyStatus is: green, if ftSecondaryLatency is less than or equal to 2 seconds; yellow, if ftSecondaryLatency is greater than 2 seconds, and less than or equal to 6 seconds; red, if ftSecondaryLatency is greater than 6 seconds; gray, if ftSecondaryLatency is unknown.
        
    
    .. py:attribute:: ftLogBandwidth
    
        The network bandwidth used for logging between the primary and secondary fault tolerance VMs. The unit is kilobytes per second.
        
    
    .. py:attribute:: ftSecondaryLatency
    
        The amount of time in wallclock that the VCPU of the secondary fault tolerance VM is behind the VCPU of the primary VM. The unit is millisecond.
        
    
    .. py:attribute:: guestHeartbeatStatus
    
        Guest operating system heartbeat metric. See guestHeartbeatStatus for a description.
        
    
    .. py:attribute:: guestMemoryUsage
    
        Guest memory utilization statistics, in MB. This is also known as active guest memory. The number can be between 0 and the configured memory size of the virtual machine. Valid while the virtual machine is running.
        
    
    .. py:attribute:: hostMemoryUsage
    
        Host memory utilization statistics, in MB. This is also known as consumed host memory. This is between 0 and the configured resource limit. Valid while the virtual machine is running. This includes the overhead memory of the VM.
        
    
    .. py:attribute:: overallCpuDemand
    
        Basic CPU performance statistics, in MHz. Valid while the virtual machine is running.
        
    
    .. py:attribute:: overallCpuUsage
    
        Basic CPU performance statistics, in MHz. Valid while the virtual machine is running.
        
    
    .. py:attribute:: privateMemory
    
        The portion of memory, in MB, that is granted to this VM from non-shared host memory.
        
    
    .. py:attribute:: sharedMemory
    
        The portion of memory, in MB, that is granted to this VM from host memory that is shared between VMs.
        
    
    .. py:attribute:: staticCpuEntitlement
    
        The static CPU resource entitlement for a virtual machine. This value is calculated based on this virtual machine's resource reservations, shares and limit, and doesn't take into account current usage. This is the worst case CPU allocation for this virtual machine, that is, the amount of CPU resource this virtual machine would receive if all virtual machines running in the cluster went to maximum consumption. Units are MHz.
        
    
    .. py:attribute:: staticMemoryEntitlement
    
        The static memory resource entitlement for a virtual machine. This value is calculated based on this virtual machine's resource reservations, shares and limit, and doesn't take into account current usage. This is the worst case memory allocation for this virtual machine, that is, the amount of memory this virtual machine would receive if all virtual machines running in the cluster went to maximum consumption. Units are MB.
        
    
    .. py:attribute:: swappedMemory
    
        The portion of memory, in MB, that is granted to this VM from the host's swap space. This is a sign that there is memory pressure on the host.
        
    
    .. py:attribute:: uptimeSeconds
    
        The system uptime of the VM in seconds.
        
    