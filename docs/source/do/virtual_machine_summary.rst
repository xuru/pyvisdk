
================================================================================
VirtualMachineSummary
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_connect_info.HostConnectInfo`,
    :py:class:`~pyvisdk.do.virtual_machine.VirtualMachine`,
    :py:class:`~pyvisdk.do.virtual_machine_usb_info.VirtualMachineUsbInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.custom_field_value.CustomFieldValue`,
    :py:class:`~pyvisdk.do.managed_entity_status.ManagedEntityStatus`,
    :py:class:`~pyvisdk.do.virtual_machine.VirtualMachine`,
    :py:class:`~pyvisdk.do.virtual_machine_config_summary.VirtualMachineConfigSummary`,
    :py:class:`~pyvisdk.do.virtual_machine_guest_summary.VirtualMachineGuestSummary`,
    :py:class:`~pyvisdk.do.virtual_machine_quick_stats.VirtualMachineQuickStats`,
    :py:class:`~pyvisdk.do.virtual_machine_runtime_info.VirtualMachineRuntimeInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_storage_summary.VirtualMachineStorageSummary`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.virtual_machine_summary.VirtualMachineSummary
    
    .. py:attribute:: config
    
        Basic configuration information about the virtual machine. This information is not available when the virtual machine is unavailable, for instance, when it is being created or deleted.
        
    
    .. py:attribute:: customValue
    
        Custom field values.
        
    
    .. py:attribute:: guest
    
        Guest operating system and VMware Tools information. See guest for more information.
        
    
    .. py:attribute:: overallStatus
    
        Overall alarm status on this node.
        
    
    .. py:attribute:: quickStats
    
        A set of statistics that are typically updated with near real-time regularity. This data object type does not support notification, for scalability reasons. Therefore, changes in QuickStats do not generate property collector updates. To monitor statistics values, use the statistics and alarms modules instead.
        
    
    .. py:attribute:: runtime
    
        Runtime and state information of a running virtual machine. Most of this information is also available when a virtual machine is powered off. In that case, it contains information from the last run, if available.
        
    
    .. py:attribute:: storage
    
        Storage information of the virtual machine. It can be explicitly refreshed with the RefreshStorageInfo operation.
        
    
    .. py:attribute:: vm
    
        Reference to the virtual machine managed object.
        
    