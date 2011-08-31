
================================================================================
VirtualMachineMemoryReservationInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_config_info.HostConfigInfo`,
    :py:class:`~pyvisdk.do.host_memory_system.HostMemorySystem`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.virtual_machine_memory_reservation_info.VirtualMachineMemoryReservationInfo
    
    .. py:attribute:: allocationPolicy
    
        Policy for allocating additional memory for virtual machines.See AllocationPolicy
        
    
    .. py:attribute:: virtualMachineMax
    
        The maximum amount of memory reserved for all running virtual machines, in bytes.
        
    
    .. py:attribute:: virtualMachineMin
    
        The minimum amount of memory reserved for all running virtual machines, in bytes.
        
    
    .. py:attribute:: virtualMachineReserved
    
        The amount of memory reserved for all running virtual machines, in bytes.
        
    