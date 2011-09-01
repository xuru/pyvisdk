
==================================================================================================
EventFilterSpecRecursionOption
==================================================================================================

.. describe:: EventFilterSpecRecursionOption

    This option specifies how to select events based on child relationships in the inventory hierarchy. If a managed entity has children, their events can be retrieved with this filter option.
    
    
    .. py:data:: EventFilterSpecRecursionOption.all
    
        Returns events pertaining either to the specified managed entity or to its child entities.
        
    
    .. py:data:: EventFilterSpecRecursionOption.children
    
        Returns events pertaining to child entities only. Excludes events pertaining to the specified managed entity itself.
        
    
    .. py:data:: EventFilterSpecRecursionOption.self
    
        Returns events that pertain only to the specified managed entity, and not its children.
        
    