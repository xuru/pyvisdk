
================================================================================
ComputeResourceConfigSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.add_standalone_host__task.AddStandaloneHost_Task`,
    :py:meth:`~pyvisdk.do.reconfigure_compute_resource__task.ReconfigureComputeResource_Task`
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.cluster_config_spec_ex.ClusterConfigSpecEx`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.compute_resource_config_spec.ComputeResourceConfigSpec
    
    .. py:attribute:: vmSwapPlacement
    
        New setting for the swapfile placement policy. Any change to this policy will affect virtual machines that subsequently power on or resume from a suspended state in this compute resource, or that migrate to a host in this compute resource while powered on; virtual machines that are currently powered on in this compute resource will not yet be affected.See VirtualMachineConfigInfoSwapPlacementType
        
    