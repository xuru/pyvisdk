
================================================================================
HostConnectInfo
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_connect_info_network_info.HostConnectInfoNetworkInfo`,
    :py:class:`~pyvisdk.do.host_datastore_connect_info.HostDatastoreConnectInfo`,
    :py:class:`~pyvisdk.do.host_license_connect_info.HostLicenseConnectInfo`,
    :py:class:`~pyvisdk.do.host_list_summary.HostListSummary`,
    :py:class:`~pyvisdk.do.virtual_machine_summary.VirtualMachineSummary`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_connection_info.QueryConnectionInfo`,
    :py:meth:`~pyvisdk.do.query_host_connection_info.QueryHostConnectionInfo`
    
.. class:: pyvisdk.do.host_connect_info.HostConnectInfo
    
    .. py:attribute:: clusterSupported
    
        Whether or not the host supports clustering capabilities such as HA or DRS and therefore can be added to a cluster. If false, the host must be added as a standalone host.
        
    
    .. py:attribute:: datastore
    
        The list of datastores on the host.
        
    
    .. py:attribute:: host
    
        Summary information about the host. The status fields and managed object reference is not set when an object of this type is created. These fields and references are typically set later when these objects are associated with a host.
        
    
    .. py:attribute:: license
    
        License manager information on the host
        
    
    .. py:attribute:: network
    
        The list of network information for networks configured on this host.
        
    
    .. py:attribute:: serverIp
    
        The IP address of the VirtualCenter already managing this host, if any.
        
    
    .. py:attribute:: vimAccountNameRequired
    
        Whether or not the host requires a vimAccountName and password to be set in the ConnectSpec. This is normally only required for VMware Server hosts.
        
    
    .. py:attribute:: vm
    
        The list of virtual machines on the host.
        
    