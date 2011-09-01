
==================================================================================================
HostConfigChangeOperation
==================================================================================================

.. describe:: HostConfigChangeOperation

    This list indicates the operation that should be performed for a network entity.
    
    
    .. py:data:: HostConfigChangeOperation.add
    
        Indicates the addition of a network entity to the configuration.
        
    
    .. py:data:: HostConfigChangeOperation.edit
    
        Indicates changes on the network entity. The entity must exist or a NotFound error will be thrown.
        
    
    .. py:data:: HostConfigChangeOperation.remove
    
        Indicates the removal of a network entity from the configuration.
        
    