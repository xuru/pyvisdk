
================================================================================
ClusterDrsVmConfigInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.cluster_config_info.ClusterConfigInfo`,
    :py:class:`~pyvisdk.do.cluster_config_info_ex.ClusterConfigInfoEx`,
    :py:class:`~pyvisdk.do.cluster_drs_vm_config_spec.ClusterDrsVmConfigSpec`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.drs_behavior.DrsBehavior`,
    :py:class:`~pyvisdk.do.virtual_machine.VirtualMachine`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.cluster_drs_vm_config_info.ClusterDrsVmConfigInfo
    
    .. py:attribute:: behavior
    
        Specifies the particular DRS behavior for this virtual machine.
        
    
    .. py:attribute:: enabled
    
        Flag to indicate whether or not VirtualCenter is allowed to perform any DRS migration or initial placement recommendations for this virtual machine. If this flag is false, the virtual machine is effectively excluded from DRS.
        
    
    .. py:attribute:: key
    
        Reference to the virtual machine.
        
    