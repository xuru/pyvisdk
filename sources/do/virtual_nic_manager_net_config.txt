
================================================================================
VirtualNicManagerNetConfig
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_virtual_nic_manager_info.HostVirtualNicManagerInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_virtual_nic.HostVirtualNic`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_net_config.QueryNetConfig`
    
.. class:: pyvisdk.do.virtual_nic_manager_net_config.VirtualNicManagerNetConfig
    
    .. py:attribute:: candidateVnic
    
        List of VirtualNic objects that may be used. This will be a subset of the list of VirtualNics in vnic.
        
    
    .. py:attribute:: multiSelectAllowed
    
        Whether multiple nics can be selected for this nicType.
        
    
    .. py:attribute:: nicType
    
        The NicType of this NetConfig.
        
    
    .. py:attribute:: selectedVnic
    
        List of VirtualNic objects that are selected for use.
        
    