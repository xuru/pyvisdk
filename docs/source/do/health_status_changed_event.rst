
================================================================================
HealthStatusChangedEvent
================================================================================


.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.event.Event`
    
.. class:: pyvisdk.do.health_status_changed_event.HealthStatusChangedEvent
    
    .. py:attribute:: componentId
    
        Unique ID of the VirtualCenter component.
        
    
    .. py:attribute:: componentName
    
        Component name.
        
    
    .. py:attribute:: newStatus
    
        Current health status of the component.
        
    
    .. py:attribute:: oldStatus
    
        Previous health status of the component.
        
    