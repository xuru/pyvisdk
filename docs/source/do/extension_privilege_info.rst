
================================================================================
ExtensionPrivilegeInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.extension.Extension`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.extension_privilege_info.ExtensionPrivilegeInfo
    
    .. py:attribute:: privGroupName
    
        Hierarchical group name. Each level of the grouping hierarchy is separated by a "." so group names may not include a ".". privGroupName.
        
    
    .. py:attribute:: privID
    
        The ID of the privilege. The format should be "<group name>.<privilege name>". The group name should be the same as the privGroupName property.
        
    