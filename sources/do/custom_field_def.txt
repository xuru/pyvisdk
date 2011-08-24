
================================================================================
CustomFieldDef
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.custom_fields_manager.CustomFieldsManager`,
    :py:class:`~pyvisdk.do.extensible_managed_object.ExtensibleManagedObject`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.privilege_policy_def.PrivilegePolicyDef`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.add_custom_field_def.AddCustomFieldDef`
    
.. class:: pyvisdk.do.custom_field_def.CustomFieldDef
    
    .. py:attribute:: fieldDefPrivileges
    
        The set of privileges to apply on this field definition
        
    
    .. py:attribute:: fieldInstancePrivileges
    
        The set of privileges to apply on instances of this field
        
    
    .. py:attribute:: key
    
        A unique ID used to reference this custom field in assignments. This ID is unique for the lifetime of the field (even across rename operations).
        
    
    .. py:attribute:: managedObjectType
    
        Type of object for which the field is valid. If not specified, the field is valid for all managed objects.
        
    
    .. py:attribute:: name
    
        Name of the field.
        
    
    .. py:attribute:: type
    
        Type of the field.
        
    