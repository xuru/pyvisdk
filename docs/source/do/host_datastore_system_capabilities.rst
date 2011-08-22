
================================================================================
HostDatastoreSystemCapabilities
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_config_info.HostConfigInfo`,
    :py:class:`~pyvisdk.do.host_datastore_system.HostDatastoreSystem`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_datastore_system_capabilities.HostDatastoreSystemCapabilities
    
    .. py:attribute:: localDatastoreSupported
    
        Indicates whether local datastores are supported.
        
    
    .. py:attribute:: nfsMountCreationRequired
    
        Indicates whether mounting the NFS volume is required to be done as part of NAS datastore creation. If this is set to true, then NAS datastores cannot be created for currently mounted NFS volumes.
        
    
    .. py:attribute:: nfsMountCreationSupported
    
        Indicates whether mounting an NFS volume is supported when a NAS datastore is created. If this option is false, then NAS datastores corresponding to NFS volumes can be created only for already mounted NFS volumes.
        
    
    .. py:attribute:: vmfsExtentExpansionSupported
    
        Indicates whether vmfs extent expansion is supported.
        
    