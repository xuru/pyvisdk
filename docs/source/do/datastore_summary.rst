
================================================================================
DatastoreSummary
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.datastore.Datastore`,
    :py:class:`~pyvisdk.do.host_datastore_connect_info.HostDatastoreConnectInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_datastore_info.VirtualMachineDatastoreInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.datastore.Datastore`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.datastore_summary.DatastoreSummary
    
    .. py:attribute:: accessible
    
        The connectivity status of this datastore. If this is set to false, meaning the datastore is not accessible, this datastore's capacity and freespace properties cannot be validated. Furthermore, if this property is set to false, some of the properties in this summary and in DatastoreInfo should not be used. Refer to the documentation for the property of your interest.
        
    
    .. py:attribute:: capacity
    
        Maximum capacity of this datastore, in bytes. This value is updated periodically by the server. It can be explicitly refreshed with the Refresh operation. This property is guaranteed to be valid only if accessible is true.
        
    
    .. py:attribute:: datastore
    
        The reference to the managed object.
        
    
    .. py:attribute:: freeSpace
    
        Available space of this datastore, in bytes. The server periodically updates this value. It can be explicitly refreshed with the Refresh operation. This property is guaranteed to be valid only if accessible is true.
        
    
    .. py:attribute:: multipleHostAccess
    
        More than one host in the datacenter has been configured with access to the datastore. This is only provided by VirtualCenter.
        
    
    .. py:attribute:: name
    
        The name of the datastore.
        
    
    .. py:attribute:: type
    
        Type of file system volume, such as VMFS or NFS.
        
    
    .. py:attribute:: uncommitted
    
        Total additional storage space, in bytes, potentially used by all virtual machines on this datastore. The server periodically updates this value. It can be explicitly refreshed with the RefreshDatastoreStorageInfo operation. This property is valid only if accessible is true.
        
    
    .. py:attribute:: url
    
        The unique locator for the datastore. This property is guaranteed to be valid only if accessible is true.
        
    