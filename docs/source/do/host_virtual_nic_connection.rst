
================================================================================
HostVirtualNicConnection
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_dns_config_spec.HostDnsConfigSpec`,
    :py:class:`~pyvisdk.do.host_ip_route_config_spec.HostIpRouteConfigSpec`,
    :py:class:`~pyvisdk.do.host_virtual_nic_manager_nic_type_selection.HostVirtualNicManagerNicTypeSelection`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.distributed_virtual_switch_port_connection.DistributedVirtualSwitchPortConnection`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_virtual_nic_connection.HostVirtualNicConnection
    
    .. py:attribute:: dvPort
    
        Identifier for the DistributedVirtualPort. If the virtual nic is to be connected to a DVS, #dvPort will be set instead of #portgroup
        
    
    .. py:attribute:: portgroup
    
        Name of the portgroup to which the virtual nic is connected to. If this parameter is set, use a virtual nic connected to a legacy portgroup.
        
    