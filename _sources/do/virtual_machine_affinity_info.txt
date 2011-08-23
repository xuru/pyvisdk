
================================================================================
VirtualMachineAffinityInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_machine_config_info.VirtualMachineConfigInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_config_spec.VirtualMachineConfigSpec`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.virtual_machine_affinity_info.VirtualMachineAffinityInfo
    
    .. py:attribute:: affinitySet
    
        List of nodes (processors for CPU, NUMA nodes for memory) that may be used by the virtual machine. If the array is empty when modifying the affinity setting, then any existing affinity is removed.
        
    