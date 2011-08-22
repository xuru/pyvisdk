
================================================================================
GuestInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_machine.VirtualMachine`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.guest_disk_info.GuestDiskInfo`,
    :py:class:`~pyvisdk.do.guest_nic_info.GuestNicInfo`,
    :py:class:`~pyvisdk.do.guest_screen_info.GuestScreenInfo`,
    :py:class:`~pyvisdk.do.guest_stack_info.GuestStackInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_tools_status.VirtualMachineToolsStatus`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.guest_info.GuestInfo
    
    .. py:attribute:: appHeartbeatStatus
    
        Application heartbeat status. Please see VirtualMachineAppHeartbeatStatusType
        
    
    .. py:attribute:: disk
    
        Guest information about disks, if known.
        
    
    .. py:attribute:: guestFamily
    
        Guest operating system family, if known.
        
    
    .. py:attribute:: guestFullName
    
        Guest operating system full name, if known.
        
    
    .. py:attribute:: guestId
    
        Guest operating system identifier (short name), if known.
        
    
    .. py:attribute:: guestState
    
        Operation mode of guest operating system. One of: * "running" - Guest is running normally. * "shuttingdown" - Guest has a pending shutdown command. * "resetting" - Guest has a pending reset command. * "standby" - Guest has a pending standby command. * "notrunning" - Guest is not running. * "unknown" - Guest information is not available.
        
    
    .. py:attribute:: hostName
    
        Hostname of the guest operating system, if known.
        
    
    .. py:attribute:: ipAddress
    
        Primary IP address assigned to the guest operating system, if known.
        
    
    .. py:attribute:: ipStack
    
        Guest information about IP networking stack, if known.
        
    
    .. py:attribute:: net
    
        Guest information about network adapters, if known.
        
    
    .. py:attribute:: screen
    
        Guest screen resolution info, if known.
        
    
    .. py:attribute:: toolsRunningStatus
    
        Current running status of VMware Tools in the guest operating system, if known. The set of possible values is described in VirtualMachineToolsRunningStatus
        
    
    .. py:attribute:: toolsStatus
    
        Current status of VMware Tools in the guest operating system, if known.
        
    
    .. py:attribute:: toolsVersion
    
        Current version of VMware Tools, if known.
        
    
    .. py:attribute:: toolsVersionStatus
    
        Current version status of VMware Tools in the guest operating system, if known. The set of possible values is described in VirtualMachineToolsVersionStatus
        
    