
================================================================================
HostNatServicePortForwardSpec
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_nat_service_spec.HostNatServiceSpec`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_nat_service_port_forward_spec.HostNatServicePortForwardSpec
    
    .. py:attribute:: guestIpAddress
    
        The IP address for the guest. Network traffic from the host is forwarded to this IP address.
        
    
    .. py:attribute:: guestPort
    
        The port number for the guest. Network traffic from the host is forwarded to this port.
        
    
    .. py:attribute:: hostPort
    
        The port number on the host. Network traffic sent to the host on this TCP/UDP port is forwarded to the guest at the specified IP address and port.
        
    
    .. py:attribute:: name
    
        The user-defined name to identify the service being forwarded. No white spaces are allowed in the string.
        
    
    .. py:attribute:: type
    
        Either "tcp" or "udp".
        
    