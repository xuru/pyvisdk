
================================================================================
VirtualMachineConfigInfo
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.query_memory_overhead_ex.QueryMemoryOverheadEx`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_machine.VirtualMachine`,
    :py:class:`~pyvisdk.do.virtual_machine_snapshot.VirtualMachineSnapshot`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.fault_tolerance_config_info.FaultToleranceConfigInfo`,
    :py:class:`~pyvisdk.do.host_cpu_id_info.HostCpuIdInfo`,
    :py:class:`~pyvisdk.do.option_value.OptionValue`,
    :py:class:`~pyvisdk.do.resource_allocation_info.ResourceAllocationInfo`,
    :py:class:`~pyvisdk.do.tools_config_info.ToolsConfigInfo`,
    :py:class:`~pyvisdk.do.virtual_hardware.VirtualHardware`,
    :py:class:`~pyvisdk.do.virtual_machine_affinity_info.VirtualMachineAffinityInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_boot_options.VirtualMachineBootOptions`,
    :py:class:`~pyvisdk.do.virtual_machine_config_info_datastore_url_pair.VirtualMachineConfigInfoDatastoreUrlPair`,
    :py:class:`~pyvisdk.do.virtual_machine_console_preferences.VirtualMachineConsolePreferences`,
    :py:class:`~pyvisdk.do.virtual_machine_default_power_op_info.VirtualMachineDefaultPowerOpInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_file_info.VirtualMachineFileInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_flag_info.VirtualMachineFlagInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_network_shaper_info.VirtualMachineNetworkShaperInfo`,
    :py:class:`~pyvisdk.do.vm_config_info.VmConfigInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.virtual_machine_config_info.VirtualMachineConfigInfo
    
    .. py:attribute:: alternateGuestName
    
        Used as display name for the operating system if guestId is
        
    
    .. py:attribute:: annotation
    
        Description for the virtual machine.
        
    
    .. py:attribute:: bootOptions
    
        Configuration options for the boot behavior of the virtual machine.
        
    
    .. py:attribute:: changeTrackingEnabled
    
        Indicates whether changed block tracking for this VM's disks is active.
        
    
    .. py:attribute:: changeVersion
    
        The changeVersion is a unique identifier for a given version of the configuration. Each change to the configuration updates this value. This is typically implemented as an ever increasing count or a time-stamp. However, a client should always treat this as an opaque string.
        
    
    .. py:attribute:: consolePreferences
    
        Legacy console viewer preferences when doing power operations.
        
    
    .. py:attribute:: cpuAffinity
    
        Affinity settings for CPU.
        
    
    .. py:attribute:: cpuAllocation
    
        Resource limits for CPU.
        
    
    .. py:attribute:: cpuFeatureMask
    
        Specifies CPU feature compatibility masks that override the defaults from the GuestOsDescriptor of the virtual machine's guest OS.
        
    
    .. py:attribute:: cpuHotAddEnabled
    
        Whether virtual processors can be added while this virtual machine is running.
        
    
    .. py:attribute:: cpuHotRemoveEnabled
    
        Whether virtual processors can be removed while this virtual machine is running.
        
    
    .. py:attribute:: datastoreUrl
    
        Enumerates the set of datastores that this virtual machine is stored on, as well as the URL identification for each of these.
        
    
    .. py:attribute:: defaultPowerOps
    
        Configuration of default power operations.
        
    
    .. py:attribute:: extraConfig
    
        Additional configuration information for the virtual machine.
        
    
    .. py:attribute:: files
    
        Information about the files associated with a virtual machine. This information does not include files for specific virtual disks or snapshots.
        
    
    .. py:attribute:: flags
    
        Additional flags for a virtual machine.
        
    
    .. py:attribute:: ftInfo
    
        Fault Tolerance settings for this virtual machine.
        
    
    .. py:attribute:: guestFullName
    
        This is the full name of the guest operating system for the virtual machine. For example: Windows 2000 Professional.
        
    
    .. py:attribute:: guestId
    
        Guest operating system configured on a virtual machine. This is a guest identifier that can be used to access the GuestOsDescriptor list for information about default configuration. For more information on possible values, see VirtualMachineGuestOsIdentifier.
        
    
    .. py:attribute:: hardware
    
        Processor, memory, and virtual devices for a virtual machine.
        
    
    .. py:attribute:: hotPlugMemoryIncrementSize
    
        Memory, in MB that can be added to a running virtual machine must be in increments of this value and needs be a multiple of this value. This value is determined by the virtual machine and is specified only if memoryHotAddEnabled has been set to true.
        
    
    .. py:attribute:: hotPlugMemoryLimit
    
        The maximum amount of memory, in MB, than can be added to a running virtual machine. This value is determined by the virtual machine and is specified only if memoryHotAddEnabled is set to true.
        
    
    .. py:attribute:: instanceUuid
    
        VirtualCenter-specific 128-bit UUID of a virtual machine, represented as a hexademical string. This identifier is used by VirtualCenter to uniquely identify all virtual machine instances, including those that may share the same SMBIOS UUID.
        
    
    .. py:attribute:: locationId
    
        Hash incorporating the virtual machine's config file location and the UUID of the host assigned to run the virtual machine.
        
    
    .. py:attribute:: memoryAffinity
    
        Affinity settings for memory.
        
    
    .. py:attribute:: memoryAllocation
    
        Resource limits for memory.
        
    
    .. py:attribute:: memoryHotAddEnabled
    
        Whether memory can be added while this virtual machine is running.
        
    
    .. py:attribute:: modified
    
        Last time a virtual machine's configuration was modified.
        
    
    .. py:attribute:: name
    
        Display name of the virtual machine.
        
    
    .. py:attribute:: networkShaper
    
        Resource limits for network.
        
    
    .. py:attribute:: npivDesiredNodeWwns
    
        The NPIV node WWNs to be extended from the original list of WWN nummbers. This property should be set to desired number which is an aggregate of existing plus new numbers. Desired Node WWNs should always be greater than the existing number of node WWNs
        
    
    .. py:attribute:: npivDesiredPortWwns
    
        The NPIV port WWNs to be extended from the original list of WWN nummbers. This property should be set to desired number which is an aggregate of existing plus new numbers. Desired Node WWNs should always be greater than the existing number of port WWNs
        
    
    .. py:attribute:: npivNodeWorldWideName
    
        A 64-bit node WWN (World Wide Name). These WWNs are paired with the npivPortWorldWideName to be used by the NPIV VPORTs instantiated for the virtual machine on the physical HBAs of the host. A pair of node and port WWNs serves as a unique identifier in accessing a LUN, so that it can be monitored or controlled by the storage administrator.
        
    
    .. py:attribute:: npivOnNonRdmDisks
    
        This property is used to check whether the NPIV can be enabled on the Virtual machine with non-rdm disks in the configuration, so this is potentially not enabling npiv on vmfs disks. Also this property is used to check whether RDM is required to generate WWNs for a virtual machine.
        
    
    .. py:attribute:: npivPortWorldWideName
    
        A 64-bit port WWN (World Wide Name). For detail description on WWN, see npivNodeWorldWideName.
        
    
    .. py:attribute:: npivTemporaryDisabled
    
        This property is used to enable or disable the NPIV capability on a desired virtual machine on a temporary basis. When this property is set NPIV Vport will not be instantiated by the VMX process of the Virtual Machine. When this property is set port WWNs and node WWNs in the VM configuration are preserved.
        
    
    .. py:attribute:: npivWorldWideNameType
    
        The source that provides/generates the assigned WWNs.
        
    
    .. py:attribute:: swapPlacement
    
        Virtual machine swapfile placement policy. This will be unset if the virtual machine's swapPlacementSupported capability is false. If swapPlacementSupported is true, the default policy is "inherit".
        
    
    .. py:attribute:: template
    
        Flag indicating whether or not a virtual machine is a template.
        
    
    .. py:attribute:: tools
    
        Configuration of VMware Tools running in the guest operating system.
        
    
    .. py:attribute:: uuid
    
        128-bit SMBIOS UUID of a virtual machine represented as a hexadecimal string in "12345678-abcd-1234-cdef-123456789abc" format.
        
    
    .. py:attribute:: vAppConfig
    
        vApp meta-data for the virtual machine
        
    
    .. py:attribute:: vAssertsEnabled
    
        Indicates whether user-configured virtual asserts will be triggered during virtual machine replay.
        
    
    .. py:attribute:: version
    
        The version string for this virtual machine.
        
    