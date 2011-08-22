
================================================================================
DatastoreCapability
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.datastore.Datastore`,
    :py:class:`~pyvisdk.do.virtual_machine_datastore_info.VirtualMachineDatastoreInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.datastore_capability.DatastoreCapability
    
    .. py:attribute:: directoryHierarchySupported
    
        Indicates whether or not directories can be created on this datastore.
        
    
    .. py:attribute:: perFileThinProvisioningSupported
    
        Indicates whether or not the datastore supports thin provisioning on a per file basis. When thin provisioning is used, backing storage is lazily allocated.
        
    
    .. py:attribute:: rawDiskMappingsSupported
    
        Indicates whether or not raw disk mappings can be created on this datastore.
        
    
    .. py:attribute:: storageIORMSupported
    
        Indicates whether the datastore supports Storage I/O Resource Management.
        
    