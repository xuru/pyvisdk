
================================================================================
VirtualMachineDefaultPowerOpInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_machine_config_info.VirtualMachineConfigInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_config_spec.VirtualMachineConfigSpec`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.virtual_machine_default_power_op_info.VirtualMachineDefaultPowerOpInfo
    
    .. py:attribute:: defaultPowerOffType
    
        Default operation for power off: soft or hard
        
    
    .. py:attribute:: defaultResetType
    
        Default operation for reset: soft or hard
        
    
    .. py:attribute:: defaultSuspendType
    
        Default operation for suspend: soft or hard
        
    
    .. py:attribute:: powerOffType
    
        Describes the default power off type for this virtual machine. The possible values are specified by the PowerOpType. * hard - Perform power off by using the PowerOff method. * soft - Perform power off by using the ShutdownGuest method. * preset - The preset value is specified in the defaultPowerOffType section. This setting is advisory and clients can choose to ignore it.
        
    
    .. py:attribute:: resetType
    
        Describes the default reset type for this virtual machine. The possible values are specified by the PowerOpType. * hard - Perform reset by using the Reset method. * soft - Perform reset by using the RebootGuest method. * preset - The preset value is specified in the defaultResetType section. This setting is advisory and clients can choose to ignore it.
        
    
    .. py:attribute:: standbyAction
    
        Behavior of virtual machine when it receives the S1 ACPI call.
        
    
    .. py:attribute:: suspendType
    
        Describes the default suspend type for this virtual machine. The possible values are specified by the PowerOpType. * hard - Perform suspend by using the Suspend method. * soft - Perform suspend by using the StandbyGuest method. * preset - The preset value is specified in the defaultSuspendType section. This setting is advisory and clients can choose to ignore it.
        
    