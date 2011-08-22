
================================================================================
VirtualMachineUsageOnDatastore
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_machine_storage_info.VirtualMachineStorageInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.datastore.Datastore`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.virtual_machine_usage_on_datastore.VirtualMachineUsageOnDatastore
    
    .. py:attribute:: committed
    
        Storage space, in bytes, on this datastore that is actually being used by the virtual machine.
        
    
    .. py:attribute:: datastore
    
        Reference to datastore for which information is being provided.
        
    
    .. py:attribute:: uncommitted
    
        Additional storage space, in bytes, potentially used by the virtual machine on this datastore.
        
    
    .. py:attribute:: unshared
    
        Storage space, in bytes, occupied by the virtual machine on this datastore that is not shared with any other virtual machine.
        
    