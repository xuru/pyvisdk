
================================================================================
HostNatServiceSpec
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_nat_service.HostNatService`,
    :py:class:`~pyvisdk.do.host_nat_service_config.HostNatServiceConfig`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_nat_service_name_service_spec.HostNatServiceNameServiceSpec`,
    :py:class:`~pyvisdk.do.host_nat_service_port_forward_spec.HostNatServicePortForwardSpec`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_nat_service_spec.HostNatServiceSpec
    
    .. py:attribute:: activeFtp
    
        The flag to indicate whether or not non-passive mode FTP connections should be allowed.
        
    
    .. py:attribute:: allowAnyOui
    
        The flag to indicate whether or not the NAT Service allows media access control traffic from any Organizational Unique Identifier (OUI)? By default, it does not allow traffic that originated from the host to avoid packet loops.
        
    
    .. py:attribute:: configPort
    
        The flag to indicate whether or not the NAT Service should open a configuration port.
        
    
    .. py:attribute:: ipGatewayAddress
    
        The IP address that the NAT Service should use on the virtual network.
        
    
    .. py:attribute:: nameService
    
        The configuration of naming services. These parameters are specific to Windows.
        
    
    .. py:attribute:: portForward
    
        The port forwarding specifications to allow network connections to be initiated from outside the firewall.
        
    
    .. py:attribute:: udpTimeout
    
        The time allotted for UDP packets.
        
    
    .. py:attribute:: virtualSwitch
    
        The name of the virtual switch to which nat service is connected.
        
    