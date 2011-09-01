
================================================================================
ResourcePoolQuickStats
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.resource_pool_summary.ResourcePoolSummary`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.resource_pool_quick_stats.ResourcePoolQuickStats
    
    .. py:attribute:: balloonedMemory
    
        The size of the balloon driver in a virtual machine, in MB. The host will inflate the balloon driver to reclaim physical memory from a virtual machine. This is a sign that there is memory pressure on the host.
        
    
    .. py:attribute:: compressedMemory
    
        The amount of compressed memory currently consumed by VM, in KB.
        
    
    .. py:attribute:: consumedOverheadMemory
    
        The amount of overhead memory, in MB, currently being consumed to run a VM. This value is limited by the overhead memory reservation for a VM, stored in overheadMemory.
        
    
    .. py:attribute:: distributedCpuEntitlement
    
        This is the amount of CPU resource, in MHz, that this VM is entitled to, as calculated by DRS. Valid only for a VM managed by DRS.
        
    
    .. py:attribute:: distributedMemoryEntitlement
    
        This is the amount of memory, in MB, that this VM is entitled to, as calculated by DRS. Valid only for a VM managed by DRS.
        
    
    .. py:attribute:: guestMemoryUsage
    
        Guest memory utilization statistics, in MB. This is also known as active guest memory. The number can be between 0 and the configured memory size of a virtual machine.
        
    
    .. py:attribute:: hostMemoryUsage
    
        Host memory utilization statistics, in MB. This is also known as consummed host memory. This is between 0 and the configured resource limit. Valid while a virtual machine is running. This includes the overhead memory of a virtual machine.
        
    
    .. py:attribute:: overallCpuDemand
    
        Basic CPU performance statistics, in MHz.
        
    
    .. py:attribute:: overallCpuUsage
    
        Basic CPU performance statistics, in MHz.
        
    
    .. py:attribute:: overheadMemory
    
        The amount of memory resource (in MB) that will be used by a virtual machine above its guest memory requirements. This value is set if and only if a virtual machine is registered on a host that supports memory resource allocation features. For powered off VMs, this is the minimum overhead required to power on the VM on the registered host. For powered on VMs, this is the current overhead reservation, a value which is almost always larger than the minimum overhead, and which grows with time.See QueryMemoryOverheadEx
        
    
    .. py:attribute:: privateMemory
    
        The portion of memory, in MB, that is granted to a virtual machine from non-shared host memory.
        
    
    .. py:attribute:: sharedMemory
    
        The portion of memory, in MB, that is granted to a virtual machine from host memory that is shared between VMs.
        
    
    .. py:attribute:: staticCpuEntitlement
    
        The static CPU resource entitlement for a virtual machine. This value is calculated based on this virtual machine's resource reservations, shares and limit, and doesn't take into account current usage. This is the worst case CPU allocation for this virtual machine, that is, the amount of CPU resource this virtual machine would receive if all virtual machines running in the cluster went to maximum consumption. Units are MHz.
        
    
    .. py:attribute:: staticMemoryEntitlement
    
        The static memory resource entitlement for a virtual machine. This value is calculated based on this virtual machine's resource reservations, shares and limit, and doesn't take into account current usage. This is the worst case memory allocation for this virtual machine, that is, the amount of memory this virtual machine would receive if all virtual machines running in the cluster went to maximum consumption. Units are MB.
        
    
    .. py:attribute:: swappedMemory
    
        The portion of memory, in MB, that is granted to a virtual machine from the host's swap space. This is a sign that there is memory pressure on the host.
        
    