
================================================================================
FaultToleranceConfigInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_machine_config_info.VirtualMachineConfigInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_config_spec.VirtualMachineConfigSpec`,
    :py:class:`~pyvisdk.do.virtual_machine_config_summary.VirtualMachineConfigSummary`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.fault_tolerance_primary_config_info.FaultTolerancePrimaryConfigInfo`,
    :py:class:`~pyvisdk.do.fault_tolerance_secondary_config_info.FaultToleranceSecondaryConfigInfo`
    
.. class:: pyvisdk.do.fault_tolerance_config_info.FaultToleranceConfigInfo
    
    .. py:attribute:: configPaths
    
        The configuration file path for all the VMs in this fault tolerance group.
        
    
    .. py:attribute:: instanceUuids
    
        The instanceUuid of all the VMs in this fault tolerance group. The first element is the instanceUuid of the primary VM.
        
    
    .. py:attribute:: role
    
        The index of the current VM in instanceUuids array starting from 1, so 1 means that it is the primary VM.
        
    