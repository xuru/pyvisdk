
================================================================================
Permission
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.reset_entity_permissions.ResetEntityPermissions`,
    :py:meth:`~pyvisdk.do.set_entity_permissions.SetEntityPermissions`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_enable_admin_failed_event.HostEnableAdminFailedEvent`,
    :py:class:`~pyvisdk.do.host_security_spec.HostSecuritySpec`,
    :py:class:`~pyvisdk.do.managed_entity.ManagedEntity`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.managed_entity.ManagedEntity`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.retrieve_all_permissions.RetrieveAllPermissions`,
    :py:meth:`~pyvisdk.do.retrieve_entity_permissions.RetrieveEntityPermissions`,
    :py:meth:`~pyvisdk.do.retrieve_role_permissions.RetrieveRolePermissions`
    
.. class:: pyvisdk.do.permission.Permission
    
    .. py:attribute:: entity
    
        Managed entity the permission is defined on. Left unset when calling setPermissions or resetPermissions, but present for the results of permission queries.
        
    
    .. py:attribute:: group
    
        Whether principal refers to a user or a group. True for a group and false for a user.
        
    
    .. py:attribute:: principal
    
        User or group receiving access in the form of "login" for local or "DOMAIN\login" for users in a Windows domain.
        
    
    .. py:attribute:: propagate
    
        Whether or not this permission propagates down the hierarchy to sub-entities.
        
    
    .. py:attribute:: roleId
    
        Reference to the role providing the access.
        
    