
================================================================================
HostVirtualNicConfig
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_network_config.HostNetworkConfig`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_virtual_nic_spec.HostVirtualNicSpec`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_virtual_nic_config.HostVirtualNicConfig
    
    .. py:attribute:: changeOperation
    
        The change operation to apply on this configuration specification.
        
    
    .. py:attribute:: device
    
        VirtualNic device to which configuration applies.
        
    
    .. py:attribute:: portgroup
    
        If the vnic is connecting to a vSwitch, this property is the name of portgroup connected. If the vnic is connecting to a DistributedVirtualSwitch, this property is ignored.
        
    
    .. py:attribute:: spec
    
        The specification of the virtual network adapter.
        
    