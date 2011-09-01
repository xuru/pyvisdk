
==================================================================================================
DiagnosticPartitionStorageType
==================================================================================================

.. describe:: DiagnosticPartitionStorageType

    Type of partition indicating the type of storage on which the partition resides. If the diagnostic partition is local only, it will only need one slot. If the diagnostic partition is on shared storage, it could be used by multiple hosts. As a result, it will need multiple slots.
    
    
    .. py:data:: DiagnosticPartitionStorageType.directAttached
    
        
        
    
    .. py:data:: DiagnosticPartitionStorageType.networkAttached
    
        
        
    