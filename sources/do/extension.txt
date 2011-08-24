
================================================================================
Extension
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.extension_manager.ExtensionManager`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.find_extension.FindExtension`
    
.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.register_extension.RegisterExtension`,
    :py:meth:`~pyvisdk.do.update_extension.UpdateExtension`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.description.Description`,
    :py:class:`~pyvisdk.do.extension_client_info.ExtensionClientInfo`,
    :py:class:`~pyvisdk.do.extension_event_type_info.ExtensionEventTypeInfo`,
    :py:class:`~pyvisdk.do.extension_fault_type_info.ExtensionFaultTypeInfo`,
    :py:class:`~pyvisdk.do.extension_health_info.ExtensionHealthInfo`,
    :py:class:`~pyvisdk.do.extension_privilege_info.ExtensionPrivilegeInfo`,
    :py:class:`~pyvisdk.do.extension_resource_info.ExtensionResourceInfo`,
    :py:class:`~pyvisdk.do.extension_server_info.ExtensionServerInfo`,
    :py:class:`~pyvisdk.do.extension_task_type_info.ExtensionTaskTypeInfo`
    
.. class:: pyvisdk.do.extension.Extension
    
    .. py:attribute:: client
    
        Clients for this extension.
        
    
    .. py:attribute:: company
    
        Company information.
        
    
    .. py:attribute:: description
    
        Description of extension.
        
    
    .. py:attribute:: eventList
    
        Definitions of events defined by this extension.
        
    
    .. py:attribute:: faultList
    
        Definitions of faults defined by this extension.
        
    
    .. py:attribute:: healthInfo
    
        Health specification provided by this extension.
        
    
    .. py:attribute:: key
    
        Extension key. Should follow java package naming conventions for uniqueness (e.g. "com.example.management").
        
    
    .. py:attribute:: lastHeartbeatTime
    
        Last extension heartbeat time.
        
    
    .. py:attribute:: privilegeList
    
        Definitions privileges defined by this extension.
        
    
    .. py:attribute:: resourceList
    
        Resource data for all locales
        
    
    .. py:attribute:: server
    
        Servers for this extension.
        
    
    .. py:attribute:: subjectName
    
        Subject name from client certificate.
        
    
    .. py:attribute:: taskList
    
        Definitions of tasks defined by this extension.
        
    
    .. py:attribute:: type
    
        Type of extension (example may include CP-DVS, NUOVA-DVS, etc.).
        
    
    .. py:attribute:: version
    
        Extension version number as a dot-separated string. For example, "1.0.0"
        
    