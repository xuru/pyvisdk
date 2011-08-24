
================================================================================
HostConnectSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.add_host__task.AddHost_Task`,
    :py:meth:`~pyvisdk.do.add_standalone_host__task.AddStandaloneHost_Task`,
    :py:meth:`~pyvisdk.do.reconnect_host__task.ReconnectHost_Task`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.folder.Folder`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_connect_spec.HostConnectSpec
    
    .. py:attribute:: force
    
        If this flag is set to "true", then the connection succeeds even if the host is already being managed by another VirtualCenter server. The original VirtualCenter server loses connection to the host.
        
    
    .. py:attribute:: hostName
    
        The DNS name or IP address of the host. (Required for adding a host.)
        
    
    .. py:attribute:: managementIp
    
        The IP address of the VirtualCenter server that will manage this host. This field can be used to control which IP address the VirtualCenter agent will send heartbeats to. If it is not set, VirtualCenter will use the local IP address used when communicating with the host. Setting this field is useful when the VirtualCenter server is behind a NAT in which case the external NAT address must be used.
        
    
    .. py:attribute:: password
    
        The password for the administration account. (Required for adding a host.)
        
    
    .. py:attribute:: port
    
        The port number for the connection. If this is not specified, the default port number is used. For ESX 2.x hosts this is the authd port (902 by default). For ESX 3.x and above and VMware Server hosts this is the https port (443 by default). If this is a reconnect, the port number is unchanged.
        
    
    .. py:attribute:: sslThumbprint
    
        The thumbprint of the SSL certificate, which the host is expected to have. If this value is set and matches the certificate thumbprint presented by the host, then the host is authenticated. If this value is not set or does not match the certificate thumbprint presented by the host, then the host's certificate is verified by checking whether it was signed by a recognized CA.
        
    
    .. py:attribute:: userName
    
        The administration account on the host. (Required for adding a host.)
        
    
    .. py:attribute:: vimAccountName
    
        The username to be used for accessing the virtual machine files on the disk.
        
    
    .. py:attribute:: vimAccountPassword
    
        The password to be used with the vimAccountName property for accessing the virtual machine files on the disk.
        
    
    .. py:attribute:: vmFolder
    
        The folder in which to store the existing virtual machines on the host. If this folder is not specified, a default folder is chosen (and possibly created) by the VirtualCenter. This folder exists (or is possibly created) on the VirtualCenter server and is called "Discovered VM".
        
    