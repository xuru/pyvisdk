
================================================================================
HostVMotionNetConfig
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_v_motion_info.HostVMotionInfo`,
    :py:class:`~pyvisdk.do.host_v_motion_system.HostVMotionSystem`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_virtual_nic.HostVirtualNic`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_v_motion_net_config.HostVMotionNetConfig
    
    .. py:attribute:: candidateVnic
    
        List of VirtualNic objects that may be used for VMotion. This will be a subset of the list of VirtualNics in vnic.
        
    
    .. py:attribute:: selectedVnic
    
        VirtualNic that is selected for use in VMotion operations.
        
    