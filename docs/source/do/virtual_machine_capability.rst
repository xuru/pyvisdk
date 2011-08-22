
================================================================================
VirtualMachineCapability
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_machine.VirtualMachine`,
    :py:class:`~pyvisdk.do.virtual_machine_config_option.VirtualMachineConfigOption`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.virtual_machine_capability.VirtualMachineCapability
    
    .. py:attribute:: bootOptionsSupported
    
        Indicates whether boot options can be configured for this virtual machine.
        
    
    .. py:attribute:: bootRetryOptionsSupported
    
        Indicates whether automatic boot retry can be configured for this virtual machine.
        
    
    .. py:attribute:: changeTrackingSupported
    
        Indicates that change tracking is supported for virtual disks of this virtual machine. However, even if change tracking is supported, it might not be available for all disks of the virtual machine. For example, passthru raw disk mappings or disks backed by any Ver1BackingInfo cannot be tracked.
        
    
    .. py:attribute:: consolePreferencesSupported
    
        Indicates whether console preferences can be set for this virtual machine.
        
    
    .. py:attribute:: cpuFeatureMaskSupported
    
        Indicates whether CPU feature requirements masks can be set for this virtual machine.
        
    
    .. py:attribute:: disableSnapshotsSupported
    
        Indicates whether or not snapshots can be disabled.
        
    
    .. py:attribute:: diskSharesSupported
    
        Indicates whether resource settings for disks can be applied to this virtual machine.
        
    
    .. py:attribute:: lockSnapshotsSupported
    
        Indicates whether or not the snapshot tree can be locked.
        
    
    .. py:attribute:: memorySnapshotsSupported
    
        Indicates whether or not a virtual machine supports memory snapshots.
        
    
    .. py:attribute:: multipleSnapshotsSupported
    
        Indicates whether or not a virtual machine supports multiple snapshots. This value is not set when the virtual machine is unavailable, for instance, when it is being created or deleted.
        
    
    .. py:attribute:: npivWwnOnNonRdmVmSupported
    
        Supports assigning NPIV WWN to virtual machines that don't have RDM disks.
        
    
    .. py:attribute:: poweredOffSnapshotsSupported
    
        Indicates whether or not a virtual machine supports snapshot operations in poweredOff state. This flag doesn't affect vim.VirtualMachine.GetSnapshot, which is always supported.
        
    
    .. py:attribute:: quiescedSnapshotsSupported
    
        Indicates whether or not a virtual machine supports quiesced snapshots.
        
    
    .. py:attribute:: recordReplaySupported
    
        Indicates whether record and replay functionality is supported on this virtual machine.
        
    
    .. py:attribute:: revertToSnapshotSupported
    
        Indicates whether or not a virtual machine supports reverting to a snapshot.
        
    
    .. py:attribute:: s1AcpiManagementSupported
    
        Indicates whether or not a virtual machine supports ACPI S1 settings management.
        
    
    .. py:attribute:: settingDisplayTopologySupported
    
        Indicates whether of not this virtual machine supports setting the display topology of the console window. This capability depends on the guest operating system configured for this virtual machine.
        
    
    .. py:attribute:: settingScreenResolutionSupported
    
        Indicates whether of not this virtual machine supports setting the screen resolution of the console window. This capability depends on the guest operating system configured for this virtual machine.
        
    
    .. py:attribute:: settingVideoRamSizeSupported
    
        Flag indicating whether the video ram size of this virtual machine can be configured.
        
    
    .. py:attribute:: snapshotConfigSupported
    
        Indicates whether or not a virtual machine supports snapshot config.
        
    
    .. py:attribute:: snapshotOperationsSupported
    
        Indicates whether or not a virtual machine supports snapshot operations.
        
    
    .. py:attribute:: swapPlacementSupported
    
        Flag indicating whether the virtual machine has a configurable swapfile placement policy.
        
    
    .. py:attribute:: toolsAutoUpdateSupported
    
        Supports tools auto-update.
        
    
    .. py:attribute:: toolsSyncTimeSupported
    
        Indicates whether asking tools to sync time with the host is supported.
        
    
    .. py:attribute:: virtualMmuUsageSupported
    
        Indicates whether or not the use of nested page table hardware support can be explicitly set.
        
    
    .. py:attribute:: vmNpivWwnDisableSupported
    
        Indicates whether the NPIV disabling operation is supported the virtual machine.
        
    
    .. py:attribute:: vmNpivWwnSupported
    
        Supports virtual machine NPIV WWN.
        
    
    .. py:attribute:: vmNpivWwnUpdateSupported
    
        Indicates whether the update of NPIV WWNs are supported on the virtual machine.
        
    