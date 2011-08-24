
================================================================================
DatastoreInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.datastore.Datastore`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.local_datastore_info.LocalDatastoreInfo`,
    :py:class:`~pyvisdk.do.nas_datastore_info.NasDatastoreInfo`,
    :py:class:`~pyvisdk.do.vmfs_datastore_info.VmfsDatastoreInfo`
    
.. class:: pyvisdk.do.datastore_info.DatastoreInfo
    
    .. py:attribute:: freeSpace
    
        Free space of this datastore, in bytes. The server periodically updates this value. It can be explicitly refreshed with the Refresh operation.
        
    
    .. py:attribute:: maxFileSize
    
        The maximum size of a file that can reside on this file system volume.
        
    
    .. py:attribute:: name
    
        The name of the datastore.
        
    
    .. py:attribute:: timestamp
    
        Time when the free-space and capacity values in DatastoreInfo and DatastoreSummary were updated.
        
    
    .. py:attribute:: url
    
        The unique locator for the datastore.
        
    