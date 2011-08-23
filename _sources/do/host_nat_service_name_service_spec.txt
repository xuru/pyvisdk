
================================================================================
HostNatServiceNameServiceSpec
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_nat_service_spec.HostNatServiceSpec`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_nat_service_name_service_spec.HostNatServiceNameServiceSpec
    
    .. py:attribute:: dnsAutoDetect
    
        The flag to indicate whether or not the DNS server should be automatically detected or specified explicitly.
        
    
    .. py:attribute:: dnsNameServer
    
        The list of DNS servers.
        
    
    .. py:attribute:: dnsPolicy
    
        The policy to use when multiple DNS addresses are available on the host.
        
    
    .. py:attribute:: dnsRetries
    
        The number of retries before giving up on a DNS request from a virtual network.
        
    
    .. py:attribute:: dnsTimeout
    
        The time (in seconds) before retrying a DNS request to an external network.
        
    
    .. py:attribute:: nbdsTimeout
    
        The time (in seconds) allotted for queries to the NetBIOS Datagram Server (NBDS).
        
    
    .. py:attribute:: nbnsRetries
    
        Number of retries for each query to the NBNS.
        
    
    .. py:attribute:: nbnsTimeout
    
        The time (in seconds) allotted for queries to the NBNS.
        
    