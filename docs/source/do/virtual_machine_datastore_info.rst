
================================================================================
VirtualMachineDatastoreInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.config_target.ConfigTarget`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.datastore_capability.DatastoreCapability`,
    :py:class:`~pyvisdk.do.datastore_summary.DatastoreSummary`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_machine_target_info.VirtualMachineTargetInfo`
    
.. class:: pyvisdk.do.virtual_machine_datastore_info.VirtualMachineDatastoreInfo
    
    .. py:attribute:: capability
    
        Information about the datastore capabilities
        
    
    .. py:attribute:: datastore
    
        Information about the datastore
        
    
    .. py:attribute:: maxFileSize
    
        The maximum size of a file that can reside on this datastore.
        
    
    .. py:attribute:: mode
    
        Access mode for this datastore. This is either readOnly or readWrite. A virtual disk needs to be stored on readWrite datastore. ISOs can be read from a readOnly datastore.See HostMountMode
        
    