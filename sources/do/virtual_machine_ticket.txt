
================================================================================
VirtualMachineTicket
================================================================================


.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.acquire_ticket.AcquireTicket`
    
.. class:: pyvisdk.do.virtual_machine_ticket.VirtualMachineTicket
    
    .. py:attribute:: cfgFile
    
        The name of the configuration file for the virtual machine.
        
    
    .. py:attribute:: host
    
        The host with which to establish a connection. If the host is not specified, it is assumed that the requesting entity knows the appropriate host with which to connect.
        
    
    .. py:attribute:: port
    
        The port number to use. If the port is not specified, it is assumed that the requesting entity knows the appropriate port to use when making a new connection.
        
    
    .. py:attribute:: sslThumbprint
    
        The expected thumbprint of the SSL cert of the host to which we are connecting.
        
    
    .. py:attribute:: ticket
    
        The ticket name. This is used as the username and password for the MKS connection.
        
    