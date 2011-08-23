
================================================================================
ResourceAllocationInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.resource_config_spec.ResourceConfigSpec`,
    :py:class:`~pyvisdk.do.virtual_machine_config_info.VirtualMachineConfigInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_config_spec.VirtualMachineConfigSpec`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.shares_info.SharesInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.resource_allocation_info.ResourceAllocationInfo
    
    .. py:attribute:: expandableReservation
    
        In a resource pool with an expandable reservation, the reservation on a resource pool can grow beyond the specified value, if the parent resource pool has unreserved resources. A non-expandable reservation is called a fixed reservation. This property is ignored for virtual machines.
        
    
    .. py:attribute:: limit
    
        The utilization of a virtual machine/resource pool will not exceed this limit, even if there are available resources. This is typically used to ensure a consistent performance of virtual machines / resource pools independent of available resources. If set to -1, then there is no fixed limit on resource usage (only bounded by available resources and shares). Units are MB for memory, MHz for CPU.
        
    
    .. py:attribute:: overheadLimit
    
        The maximum allowed overhead memory. For a powered on virtual machine, the overhead memory reservation cannot be larger than its overheadLimit. This property is only applicable to powered on virtual machines and is not persisted across reboots. This property is not applicable for resource pools. If set to -1, then there is no limit on reservation. Units are MB.
        
    
    .. py:attribute:: reservation
    
        Amount of resource that is guaranteed available to the virtual machine or resource pool. Reserved resources are not wasted if they are not used. If the utilization is less than the reservation, the resources can be utilized by other running virtual machines. Units are MB for memory, MHz for CPU.
        
    
    .. py:attribute:: shares
    
        Memory shares are used in case of resource contention.
        
    