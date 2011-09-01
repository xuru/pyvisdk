
================================================================================
EventEx
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.key_any_value.KeyAnyValue`,
    :py:class:`~pyvisdk.do.localized_method_fault.LocalizedMethodFault`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.event.Event`
    
.. class:: pyvisdk.do.event_ex.EventEx
    
    .. py:attribute:: arguments
    
        The event arguments associated with the event
        
    
    .. py:attribute:: eventTypeId
    
        The type of the event.
        
    
    .. py:attribute:: fault
    
        The fault that triggered the event, if any
        
    
    .. py:attribute:: message
    
        An arbitrary message string, not localized.
        
    
    .. py:attribute:: objectId
    
        The ID of the object (VM, Host, Folder..) which the event pertains to. Federated or local inventory path.
        
    
    .. py:attribute:: objectName
    
        The name of the object
        
    
    .. py:attribute:: objectType
    
        the type of the object, if known to the VirtualCenter inventory
        
    
    .. py:attribute:: severity
    
        The severity level of the message: null=>info.See EventEventSeverity
        
    