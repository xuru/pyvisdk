
================================================================================
VirtualMachineFlagInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_machine_config_info.VirtualMachineConfigInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_config_spec.VirtualMachineConfigSpec`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.virtual_machine_flag_info.VirtualMachineFlagInfo
    
    .. py:attribute:: disableAcceleration
    
        Flag to turn off video acceleration for a virtual machine console window.
        
    
    .. py:attribute:: diskUuidEnabled
    
        Indicates whether disk UUIDs are being used by this virtual machine. If this flag is set to false, disk UUIDs are not exposed to the guest.
        
    
    .. py:attribute:: enableLogging
    
        Flag to enable logging for a virtual machine.
        
    
    .. py:attribute:: htSharing
    
        Specifies how the VCPUs of a virtual machine are allowed to share physical cores on a hyperthreaded system. Two VCPUs are "sharing" a core if they are both running on logical CPUs of the core at the same time.
        
    
    .. py:attribute:: monitorType
    
        Virtual machine monitor type. See VirtualMachineFlagInfoMonitorType for possible values for this property.
        
    
    .. py:attribute:: recordReplayEnabled
    
        Flag to specify whether record and replay operations are allowed for this virtual machine. If this flag is set to 'true', instruction virtualization will use hardware virtualization (HV) support. I.e., virtualExecUsage will be set to 'hvOn'. If this flag is set to 'false' for a virtual machine that already has a recording, replay will be disallowed, though the recording will be preserved. If the value is unset, the behavior 'false' will be used.
        
    
    .. py:attribute:: runWithDebugInfo
    
        Flag to specify whether or not to run in debug mode.
        
    
    .. py:attribute:: snapshotDisabled
    
        Flag to specify whether snapshots are disabled for this virtual machine.
        
    
    .. py:attribute:: snapshotLocked
    
        Flag to specify whether the snapshot tree is locked for this virtual machine.
        
    
    .. py:attribute:: snapshotPowerOffBehavior
    
        Specifies the power-off behavior for a virtual machine that has a snapshot. If the value is unset, the behavior 'powerOff' will be used.
        
    
    .. py:attribute:: useToe
    
        Flag to specify whether or not to use TOE (TCP/IP Offloading).
        
    
    .. py:attribute:: virtualExecUsage
    
        Indicates whether or not the system will try to use Hardware Virtualization (HV) support for instruction virtualization, if available.
        
    
    .. py:attribute:: virtualMmuUsage
    
        Indicates whether or not the system will try to use nested page table hardware support, if available.
        
    