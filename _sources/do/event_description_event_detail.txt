
================================================================================
EventDescriptionEventDetail
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.event_description.EventDescription`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.event_description_event_detail.EventDescriptionEventDetail
    
    .. py:attribute:: category
    
        A category of events.
        
    
    .. py:attribute:: description
    
        A string that is a short human-parseable description of the event.
        
    
    .. py:attribute:: formatOnComputeResource
    
        A string that is appropriate in the context of a specific cluster. For example, a powering on event in this context produces the following string:
        
    
    .. py:attribute:: formatOnDatacenter
    
        A string that is appropriate in the context of a specific Datacenter. For example, a renaming event in this context produces the following string:
        
    
    .. py:attribute:: formatOnHost
    
        A string that is appropriate in the context of a specific Host. For example, a powering on event in this context produces the following string:
        
    
    .. py:attribute:: formatOnVm
    
        A string that is appropriate for the context of a specific virtual machine. For example, a powering on event in this context produces the following string:
        
    
    .. py:attribute:: fullFormat
    
        A string whose context is not entity-specific. For example, a powering on event produces the following string:
        
    
    .. py:attribute:: key
    
        Type of event being described.
        
    
    .. py:attribute:: longDescription
    
        A detailed description of the event. It includes common causes and actions to remediate them. It may also include links to kb articles and other diagnostic information. For example, the BadUserNameSessionEvent may produce the following string:
        
    