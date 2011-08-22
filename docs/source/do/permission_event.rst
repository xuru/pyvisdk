
================================================================================
PermissionEvent
================================================================================


.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.permission_added_event.PermissionAddedEvent`,
    :py:class:`~pyvisdk.do.permission_removed_event.PermissionRemovedEvent`,
    :py:class:`~pyvisdk.do.permission_updated_event.PermissionUpdatedEvent`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.managed_entity_event_argument.ManagedEntityEventArgument`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.authorization_event.AuthorizationEvent`
    
.. class:: pyvisdk.do.permission_event.PermissionEvent
    
    .. py:attribute:: entity
    
        The entity to which the permission applied.
        
    
    .. py:attribute:: group
    
        Whether or not the principal was a group.
        
    
    .. py:attribute:: principal
    
        The user name or group to which the permission was granted.
        
    