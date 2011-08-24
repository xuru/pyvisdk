
================================================================================
EventArgDesc
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.element_description.ElementDescription`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.retrieve_argument_description.RetrieveArgumentDescription`
    
.. class:: pyvisdk.do.event_arg_desc.EventArgDesc
    
    .. py:attribute:: description
    
        The localized description of the event argument. The key holds the localization prefix for the argument, which is decided by the Event type that it is actually declared in, which may be a base type of this event type.
        
    
    .. py:attribute:: name
    
        The name of the argument
        
    
    .. py:attribute:: type
    
        The type of the argument. The supported values are
        
    