
==================================================================================================
ObjectUpdateKind
==================================================================================================

.. describe:: ObjectUpdateKind

    Enumeration of different kinds of updates.
    
    
    .. py:data:: ObjectUpdateKind.enter
    
        A managed object became visible to a filter for the first time. For instance, this can happen if a virtual machine is added to a folder.
        
    
    .. py:data:: ObjectUpdateKind.leave
    
        A managed object left the set of objects visible to a filter. For instance, this can happen when a virtual machine is destroyed.
        
    
    .. py:data:: ObjectUpdateKind.modify
    
        A property of the managed object changed its value.
        
    