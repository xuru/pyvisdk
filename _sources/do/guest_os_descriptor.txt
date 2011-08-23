
================================================================================
GuestOsDescriptor
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_machine_config_option.VirtualMachineConfigOption`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_cpu_id_info.HostCpuIdInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.guest_os_descriptor.GuestOsDescriptor
    
    .. py:attribute:: cpuFeatureMask
    
        Specifies the CPU feature compatibility masks.
        
    
    .. py:attribute:: family
    
        Family to which this guest operating system belongs.
        
    
    .. py:attribute:: fullName
    
        Full name of the guest operating system. For example, if the value of "id" is "win2000Pro", then the value of "fullName" is "Windows 2000 Professional".
        
    
    .. py:attribute:: id
    
        Identifier (short name) for the guest operating system.
        
    
    .. py:attribute:: recommendedColorDepth
    
        Recommended default color depth for this guest.
        
    
    .. py:attribute:: recommendedDiskController
    
        Recommended default disk controller type for this guest.
        
    
    .. py:attribute:: recommendedDiskSizeMB
    
        Recommended default disk size for this guest, in MB.
        
    
    .. py:attribute:: recommendedEthernetCard
    
        Recommended default ethernet controller type for this guest.
        
    
    .. py:attribute:: recommendedMemMB
    
        Recommended default memory size for this guest, in MB.
        
    
    .. py:attribute:: recommendedSCSIController
    
        Recommended default SCSI controller type for this guest.
        
    
    .. py:attribute:: supportedDiskControllerList
    
        List of supported disk controller types for this guest.
        
    
    .. py:attribute:: supportedEthernetCard
    
        List of supported ethernet cards for this guest.
        
    
    .. py:attribute:: supportedMaxCPUs
    
        Maximum number of processors supported for this guest.
        
    
    .. py:attribute:: supportedMaxMemMB
    
        Maximum memory requirements supported for this guest, in MB.
        
    
    .. py:attribute:: supportedMinMemMB
    
        Minimum memory requirements supported for this guest, in MB.
        
    
    .. py:attribute:: supportedNumDisks
    
        Number of disks supported for this guest.
        
    
    .. py:attribute:: supportsCpuHotAdd
    
        Whether virtual CPUs can be added to this guest while the virtual machine is running.
        
    
    .. py:attribute:: supportsCpuHotRemove
    
        Whether virtual CPUs can be removed from this guest while the virtual machine is running.
        
    
    .. py:attribute:: supportsMemoryHotAdd
    
        Whether the memory size for this guest can be changed while the virtual machine is running.
        
    
    .. py:attribute:: supportsSlaveDisk
    
        Flag to indicate whether or not this guest can support a disk configured as a slave.
        
    
    .. py:attribute:: supportsVMI
    
        Flag indicating whether or not this guest supports the virtual machine interface.
        
    
    .. py:attribute:: supportsWakeOnLan
    
        Flag to indicate whether or not this guest can support Wake-on-LAN.
        
    