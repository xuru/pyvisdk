
================================================================================
VirtualMachineConfigSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.create_child_vm__task.CreateChildVM_Task`,
    :py:meth:`~pyvisdk.do.create_vm__task.CreateVM_Task`,
    :py:meth:`~pyvisdk.do.reconfig_vm__task.ReconfigVM_Task`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_machine_clone_spec.VirtualMachineCloneSpec`,
    :py:class:`~pyvisdk.do.virtual_machine_import_spec.VirtualMachineImportSpec`,
    :py:class:`~pyvisdk.do.vm_being_created_event.VmBeingCreatedEvent`,
    :py:class:`~pyvisdk.do.vm_reconfigured_event.VmReconfiguredEvent`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.fault_tolerance_config_info.FaultToleranceConfigInfo`,
    :py:class:`~pyvisdk.do.option_value.OptionValue`,
    :py:class:`~pyvisdk.do.resource_allocation_info.ResourceAllocationInfo`,
    :py:class:`~pyvisdk.do.tools_config_info.ToolsConfigInfo`,
    :py:class:`~pyvisdk.do.virtual_device_config_spec.VirtualDeviceConfigSpec`,
    :py:class:`~pyvisdk.do.virtual_machine_affinity_info.VirtualMachineAffinityInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_boot_options.VirtualMachineBootOptions`,
    :py:class:`~pyvisdk.do.virtual_machine_console_preferences.VirtualMachineConsolePreferences`,
    :py:class:`~pyvisdk.do.virtual_machine_cpu_id_info_spec.VirtualMachineCpuIdInfoSpec`,
    :py:class:`~pyvisdk.do.virtual_machine_default_power_op_info.VirtualMachineDefaultPowerOpInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_file_info.VirtualMachineFileInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_flag_info.VirtualMachineFlagInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_network_shaper_info.VirtualMachineNetworkShaperInfo`,
    :py:class:`~pyvisdk.do.vm_config_spec.VmConfigSpec`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.virtual_machine_config_spec.VirtualMachineConfigSpec
    
    .. py:attribute:: alternateGuestName
    
        Full name for guest, if guestId is specified as
        
    
    .. py:attribute:: annotation
    
        User-provided description of the virtual machine. Because this property is optional in the virtual machine configuration, it is necessary to pass an explicit empty string in a ConfigSpec object to remove an annotation that is already present in the VirtualMachineConfigInfo for a virtual machine.
        
    
    .. py:attribute:: bootOptions
    
        Settings that control the boot behavior of the virtual machine. These settings take effect during the next power-on of the virtual machine.
        
    
    .. py:attribute:: changeTrackingEnabled
    
        Setting to control enabling/disabling changed block tracking for the virtual disks of this VM. This may only be set if the changeTrackingSupported capability is true for this virtual machine. Any change to this property will take effect the next time the virtual machine powers on, resumes from a suspended state, performs a snapshot create/delete/revert operation or migrates while powered on.
        
    
    .. py:attribute:: changeVersion
    
        If specified, the changes are only applied if the current changeVersion matches the specified changeVersion. This field can be used to guard against updates that have happened between when configInfo is read and when it is applied.
        
    
    .. py:attribute:: consolePreferences
    
        Legacy console viewer preferences that are used with power operations. For example, power on.
        
    
    .. py:attribute:: cpuAffinity
    
        Affinity settings for CPU.
        
    
    .. py:attribute:: cpuAllocation
    
        Resource limits for CPU.
        
    
    .. py:attribute:: cpuFeatureMask
    
        Specifies the CPU feature compatibility masks.
        
    
    .. py:attribute:: cpuHotAddEnabled
    
        Indicates whether or not virtual processors can be added to the virtual machine while it is running. This attribute can only be set when the virtual machine is powered-off.
        
    
    .. py:attribute:: cpuHotRemoveEnabled
    
        Indicates whether or not virtual processors can be removed from the virtual machine while it is running. This attribute can only be set when the virtual machine is powered-off.
        
    
    .. py:attribute:: deviceChange
    
        Set of virtual devices being modified by the configuration operation.
        
    
    .. py:attribute:: extraConfig
    
        Additional configuration information for the virtual machine. This describes a set of modifications to the additional options. An option is removed if the key is present but the value is not set or the value is an empty string. Otherwise, the key is set to the new value.
        
    
    .. py:attribute:: files
    
        Information about virtual machine files.
        
    
    .. py:attribute:: flags
    
        Additional flags for a virtual machine.
        
    
    .. py:attribute:: ftInfo
    
        Fault Tolerance settings for this virtual machine.
        
    
    .. py:attribute:: guestId
    
        Short guest operating system identifier.
        
    
    .. py:attribute:: instanceUuid
    
        VirtualCenter-specific 128-bit UUID of a virtual machine, represented as a hexadecimal string. This identifier is used by VirtalCenter to uniquely identify all virtual machine instances in the Virtual Infrastructure environment, including those that may share the same SMBIOS UUID.
        
    
    .. py:attribute:: locationId
    
        128-bit hash based on the virtual machine's configuration file location and the UUID of the host assigned to run the virtual machine.
        
    
    .. py:attribute:: memoryAffinity
    
        Affinity settings for memory.
        
    
    .. py:attribute:: memoryAllocation
    
        Resource limits for memory.
        
    
    .. py:attribute:: memoryHotAddEnabled
    
        Indicates whether or not memory can be added to the virtual machine while it is running. This attribute can only be set when the virtual machine is powered-off.
        
    
    .. py:attribute:: memoryMB
    
        Size of a virtual machine's memory, in MB.
        
    
    .. py:attribute:: name
    
        Display name of the virtual machine.
        
    
    .. py:attribute:: networkShaper
    
        Resource limits for network.
        
    
    .. py:attribute:: npivDesiredNodeWwns
    
        The NPIV node WWNs to be extended from the original list of WWN nummbers. This property should be set to desired number which is an aggregate of existing plus new numbers. Desired Node WWNs should always be greater than the existing number of node WWNs
        
    
    .. py:attribute:: npivDesiredPortWwns
    
        The NPIV port WWNs to be extended from the original list of WWN nummbers. This property should be set to desired number which is an aggregate of existing plus new numbers. Desired Node WWNs should always be greater than the existing number of port WWNs
        
    
    .. py:attribute:: npivNodeWorldWideName
    
        The NPIV node WWN to be assigned to a virtual machine. This property should only be used or set when the value of npivWorldWideNameOp property is "set". Otherwise, an InvalidVmConfig fault will be thrown. If the specified node WWN is currently being used by another virtual machine, a VmWwnConflict fault will be thrown.
        
    
    .. py:attribute:: npivOnNonRdmDisks
    
        This property is used to check whether the NPIV can be enabled on the Virtual machine with non-rdm disks in the configuration, so this is potentially not enabling npiv on vmfs disks. Also this property is used to check whether RDM is required to generate WWNs for a virtual machine.
        
    
    .. py:attribute:: npivPortWorldWideName
    
        The NPIV port WWN to be assigned to a virtual machine. This property should only be used or set when the value of npivWorldWideNameOp property is "set". Otherwise, an InvalidVmConfig fault will be thrown. If the specified port WWN is currently being used by another virtual machine, a VmWwnConflict fault will be thrown.
        
    
    .. py:attribute:: npivTemporaryDisabled
    
        This property is used to enable or disable the NPIV capability on a desired virtual machine on a temporary basis. When this property is set NPIV Vport will not be instantiated by the VMX process of the Virtual Machine. When this property is set port WWNs and node WWNs in the VM configuration are preserved.
        
    
    .. py:attribute:: npivWorldWideNameOp
    
        The flag to indicate what type of NPIV WWN operation is going to be performed on the virtual machine. If unset, it indicates no change to existing NPIV WWN assignment (or not assigned) in the virtual machine.
        
    
    .. py:attribute:: npivWorldWideNameType
    
        This property is used internally in the communication between the VirtualCenter server and ESX Server to indicate the source for npivNodeWorldWideName and npivPortWorldWideName when npivWorldWideNameOp is "set". This property should only be set by the VirtualCenter server.
        
    
    .. py:attribute:: numCPUs
    
        Number of virtual processors in a virtual machine.
        
    
    .. py:attribute:: powerOpInfo
    
        Configuration for default power operations.
        
    
    .. py:attribute:: swapPlacement
    
        Virtual machine swapfile placement policy. This may only be set if the swapPlacementSupported capability is true for this virtual machine. Any change to this policy will take effect the next time the virtual machine powers on, resumes from a suspended state, or migrates while powered on.
        
    
    .. py:attribute:: tools
    
        Configuration of VMware Tools running in the guest operating system.
        
    
    .. py:attribute:: uuid
    
        128-bit SMBIOS UUID of a virtual machine represented as a hexadecimal string in "12345678-abcd-1234-cdef-123456789abc" format.
        
    
    .. py:attribute:: vAppConfig
    
        Configuration of vApp meta-data for a virtual machine
        
    
    .. py:attribute:: vAppConfigRemoved
    
        Set to true, if the vApp configuration should be removed
        
    
    .. py:attribute:: vAssertsEnabled
    
        Indicates whether user-configured virtual asserts will be triggered during virtual machine replay. This setting takes effect during the next replay of the virtual machine.
        
    
    .. py:attribute:: version
    
        The version string for this virtual machine. This is used only while creating a new virtual machine, and can be updated by invoking UpgradeVM_Task for this virtual machine.
        
    