
================================================================================
ClusterDasVmConfigInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.cluster_config_info.ClusterConfigInfo`,
    :py:class:`~pyvisdk.do.cluster_config_info_ex.ClusterConfigInfoEx`,
    :py:class:`~pyvisdk.do.cluster_das_vm_config_spec.ClusterDasVmConfigSpec`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.cluster_das_vm_settings.ClusterDasVmSettings`,
    :py:class:`~pyvisdk.do.das_vm_priority.DasVmPriority`,
    :py:class:`~pyvisdk.do.virtual_machine.VirtualMachine`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.cluster_das_vm_config_info.ClusterDasVmConfigInfo
    
    .. py:attribute:: dasSettings
    
        HA settings that apply to this virtual machine.
        
    
    .. py:attribute:: key
    
        Reference to the virtual machine.
        
    
    .. py:attribute:: powerOffOnIsolation
    
        Flag to indicate whether or not the virtual machine should be powered off if a host determines that it is isolated from the rest of the compute resource.
        
    
    .. py:attribute:: restartPriority
    
        Restart priority for a virtual machine.
        
    