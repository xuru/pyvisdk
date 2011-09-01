
================================================================================
ComputeResourceConfigInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.compute_resource.ComputeResource`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.cluster_config_info_ex.ClusterConfigInfoEx`
    
.. class:: pyvisdk.do.compute_resource_config_info.ComputeResourceConfigInfo
    
    .. py:attribute:: vmSwapPlacement
    
        Swapfile placement policy for virtual machines within this compute resource. Any policy except for "inherit" is a valid value for this property; the default is "vmDirectory". This setting will be honored for each virtual machine within the compute resource for which the following is true: * The virtual machine is executing on a host that has the perVmSwapFiles capability. * The virtual machine configuration's swapPlacement property is set to "inherit". See VirtualMachineConfigInfoSwapPlacementType
        
    