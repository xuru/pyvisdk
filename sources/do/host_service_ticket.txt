
================================================================================
HostServiceTicket
================================================================================


.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.acquire_cim_services_ticket.AcquireCimServicesTicket`
    
.. class:: pyvisdk.do.host_service_ticket.HostServiceTicket
    
    .. py:attribute:: host
    
        The name of the host providing the service for which the ticket applies. If omitted, then the client uses the host name for the server that issued the ticket.
        
    
    .. py:attribute:: port
    
        Access to some services is made possible by connecting to a port on a server. If the service for which a ticket is issued is available on a particular port, that port number is specified with this property. If omitted, except in the case of connecting to CIM interfaces, the port number for the service that issued the ticket is used. In the case of connecting to a CIM interface the standard well known port for the particular service will be used for the connection.
        
    
    .. py:attribute:: service
    
        The name of the service to which to connect.
        
    
    .. py:attribute:: serviceVersion
    
        A dot-separated string identifying the service protocol version. For example, 1.0 is used for NFC hosted by vpxa on ESX 2.5, and 1.1 is used for NFC hosted by hostd on ESX 3.0.
        
    
    .. py:attribute:: sessionId
    
        An identifying string for the session created for the ticketed connection. This is used by the host service to identify the operations permitted within the session.
        
    
    .. py:attribute:: sslThumbprint
    
        The expected thumbprint of the SSL cert of the host to which we are connecting.
        
    