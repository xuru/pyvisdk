
================================================================================
DistributedVirtualSwitchHostMember
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.dvs_config_info.DVSConfigInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.distributed_virtual_switch_host_member_config_info.DistributedVirtualSwitchHostMemberConfigInfo`,
    :py:class:`~pyvisdk.do.distributed_virtual_switch_product_spec.DistributedVirtualSwitchProductSpec`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.distributed_virtual_switch_host_member.DistributedVirtualSwitchHostMember
    
    .. py:attribute:: config
    
        Host member configuration.
        
    
    .. py:attribute:: productInfo
    
        The vendor, product and version information for the proxy vSwitch module.
        
    
    .. py:attribute:: status
    
        The host DistributedVirtualSwitch component status. See HostComponentState for valid values.
        
    
    .. py:attribute:: statusDetail
    
        Additional information regarding the host's current status.
        
    
    .. py:attribute:: uplinkPortKey
    
        The port keys of the uplink ports created for the host member. These ports will be deleted after the host leaves the switch.
        
    