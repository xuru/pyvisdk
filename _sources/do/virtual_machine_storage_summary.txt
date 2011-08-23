
================================================================================
VirtualMachineStorageSummary
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_machine_summary.VirtualMachineSummary`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.virtual_machine_storage_summary.VirtualMachineStorageSummary
    
    .. py:attribute:: committed
    
        Total storage space, in bytes, committed to this virtual machine across all datastores.
        
    
    .. py:attribute:: timestamp
    
        Time when values in this structure were last updated.
        
    
    .. py:attribute:: uncommitted
    
        Additional storage space, in bytes, potentially used by this virtual machine on all datastores.
        
    
    .. py:attribute:: unshared
    
        Total storage space, in bytes, occupied by the virtual machine across all datastores, that is not shared with any other virtual machine.
        
    