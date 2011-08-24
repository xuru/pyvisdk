
================================================================================
HostCapability
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_system.HostSystem`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_cpu_id_info.HostCpuIdInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_target_capabilities.QueryTargetCapabilities`
    
.. class:: pyvisdk.do.host_capability.HostCapability
    
    .. py:attribute:: backgroundSnapshotsSupported
    
        Flag indicating whether background snapshots are supported on this host.
        
    
    .. py:attribute:: cloneFromSnapshotSupported
    
        Indicates whether or not cloning a virtual machine from a snapshot point is allowed.
        
    
    .. py:attribute:: cpuMemoryResourceConfigurationSupported
    
        Flag indicating whether cpu and memory resource configuration is supported. If this is set to false, UpdateConfig, UpdateChildResourceConfiguration cannot be used for changing the cpu/memory resource configurations.
        
    
    .. py:attribute:: datastorePrincipalSupported
    
        Flag indicating whether datastore principal user is supported on the host.
        
    
    .. py:attribute:: deltaDiskBackingsSupported
    
        Flag indicating whether explicitly creating arbirary configurations of delta disk backings is supported.
        
    
    .. py:attribute:: ftCompatibilityIssues
    
        For a host which doesn't support Fault Tolerance, indicates all the reasons for the incompatibility. HostCapabilityFtUnsupportedReason lists the set of possible values.
        
    
    .. py:attribute:: ftSupported
    
        Indicates whether this host supports Fault Tolerance There can be many reasons why a host does not support Fault Tolerance, which includes CPU compatibility, product compatibility as well as other host configuration settings. For specific reasons, look into replayCompatibilityIssues and ftCompatibilityIssues
        
    
    .. py:attribute:: highGuestMemSupported
    
        Is high guest memory supported.
        
    
    .. py:attribute:: ipmiSupported
    
        Flag indicating whether the host supports IPMI (Intelligent Platform Management Interface). XXX - Make ipmiSupported optional until there is a compatible hostagent.
        
    
    .. py:attribute:: iscsiSupported
    
        Is access to iSCSI devices supported.
        
    
    .. py:attribute:: localSwapDatastoreSupported
    
        Flag indicating whether the host supports selecting a datastore that that may be used to store virtual machine swapfiles.
        
    
    .. py:attribute:: loginBySSLThumbprintSupported
    
        Flag indicating whether this host supports SSL thumbprint authentication
        
    
    .. py:attribute:: maintenanceModeSupported
    
        Is maintenance mode supported
        
    
    .. py:attribute:: maxRunningVMs
    
        The maximum number of virtual machines that can be running simultaneously on this host. If this capability is not set, the number of virtual machines running simultaneously is unlimited.
        
    
    .. py:attribute:: maxSupportedVcpus
    
        The maximum number of virtual CPUs supported per virtual machine. If this capability is not set, the number is unlimited.
        
    
    .. py:attribute:: maxSupportedVMs
    
        The maximum number of virtual machines that can exist on this host. If this capability is not set, the number of virtual machines is unlimited.
        
    
    .. py:attribute:: nfsSupported
    
        Is access to NFS devices supported.
        
    
    .. py:attribute:: nicTeamingSupported
    
        Is NIC teaming supported.
        
    
    .. py:attribute:: perVMNetworkTrafficShapingSupported
    
        Indicates whether network traffic shaping on a per virtual machine basis is supported.
        
    
    .. py:attribute:: perVmSwapFiles
    
        Flag indicating whether virtual machine execution on this host involves a swapfile for each virtual machine. If true, the swapfile placement for a powered-on virtual machine is advertised in its FileLayout by the swapFile property.
        
    
    .. py:attribute:: preAssignedPCIUnitNumbersSupported
    
        Flag to indicate whether the server returns unit numbers in a pre-assigned range for devices on the PCI bus. When the server supports this flag, the device unit number namespace is partitioned by device type. Different types of devices will sit in a specific range of unit numbers that may not correspond to physical slots in the pci bus but present a relative ordering of the devices with respect to other devices of the same type. Note that this does not mean that the user can set the relative ordering between device types, but only allows stable orderings between devices of the same type. The unit number will now clearly represent an ordering between devices of the same type. unitNumber This property is only available for devices on the pci controller.
        
    
    .. py:attribute:: rebootSupported
    
        Flag indicating whether rebooting the host is supported.
        
    
    .. py:attribute:: recordReplaySupported
    
        Indicates whether this host supports record and replay
        
    
    .. py:attribute:: recursiveResourcePoolsSupported
    
        
        
    
    .. py:attribute:: replayCompatibilityIssues
    
        For a host which doesn't support replay, indicates all the reasons for the incompatibility. HostReplayUnsupportedReason lists the set of possible values.
        
    
    .. py:attribute:: replayUnsupportedReason
    
        For a host whose CPU doesn't support replay, indicates the reason for the incompatibility. HostReplayUnsupportedReason represents the set of possible values.
        
    
    .. py:attribute:: restrictedSnapshotRelocateSupported
    
        Indicates whether this host supports relocation of virtual machines with snapshots. Must be true on the source and destination hosts for the relocation to work. Even if this is true, the following conditions must hold: 1) All the the vm's files are in one directory prior to the relocate. 2) All of the vm's files will be in one directory after the relocate. 3) The source and destination hosts are the same product version.
        
    
    .. py:attribute:: sanSupported
    
        Flag indicating whether access to SAN devices is supported.
        
    
    .. py:attribute:: scaledScreenshotSupported
    
        Indicates whether scaling is supported for screenshots retrieved over https. If true, screenshot retrieval supports the additional optional parameters 'width' and 'height'. After cropping, the returned image will be scaled to these dimensions. If only one of these parameters is specified, default behavior is to return an image roughly proportional to the source image.
        
    
    .. py:attribute:: screenshotSupported
    
        Indicates whether the screenshot retrival over https is supported for this host's virtual machines. If true, a screenshot can be retrieved at the HTTPS relative path
        
    
    .. py:attribute:: shutdownSupported
    
        Flag indicating whether the host can be powered off
        
    
    .. py:attribute:: standbySupported
    
        Flag indicating whether you can put the host in a power down state, from which it can be powered up automatically.
        
    
    .. py:attribute:: storageIORMSupported
    
        Indicates whether the host supports storage I/O resource management.
        
    
    .. py:attribute:: storageVMotionSupported
    
        Indicates whether the storage of a powered-on virtual machine may be relocated.
        
    
    .. py:attribute:: supportedCpuFeature
    
        CPU feature set that is supported by the virtualization platform. This feature set may reflect characteristics of the product capabilities and licensing. For any feature marked '-', reference the cpuFeature array of the host's HardwareInfo to determine the correct value.
        
    
    .. py:attribute:: suspendedRelocateSupported
    
        Indicates whether this host supports relocation of suspended virtual machines. Must be true on the source and destination hosts for the relocation to work.
        
    
    .. py:attribute:: tpmSupported
    
        Flag indicating whether this host supports the integrity measurement using a TPM device.
        
    
    .. py:attribute:: unsharedSwapVMotionSupported
    
        Flag indicating whether the host supports participating in a VMotion where the virtual machine swapfile is not visible to the destination.
        
    
    .. py:attribute:: virtualExecUsageSupported
    
        Indicates whether the host supports configuring hardware virtualization (HV) support for virtual machines.
        
    
    .. py:attribute:: vlanTaggingSupported
    
        Is VLAN Tagging supported.
        
    
    .. py:attribute:: vmDirectPathGen2Supported
    
        Indicates whether the host supports network passthrough using VMDirectPath Gen 2. Note that this is a general capability for the host and is independent of support by a given physical NIC. If false, the reason(s) for lack of support will be provided in vmDirectPathGen2UnsupportedReason and/or in vmDirectPathGen2UnsupportedReasonExtended.
        
    
    .. py:attribute:: vmDirectPathGen2UnsupportedReason
    
        If vmDirectPathGen2Supported is false, this array will be populated with reasons for the lack of support (chosen from VmDirectPathGen2UnsupportedReason). If there is a reason for the lack of support that cannot be described by the available constants, vmDirectPathGen2UnsupportedReasonExtended will be populated with an additional explanation provided by the platform.
        
    
    .. py:attribute:: vmDirectPathGen2UnsupportedReasonExtended
    
        If vmDirectPathGen2Supported is false, this property may contain an explanation provided by the platform, beyond the reasons (if any) enumerated in vmDirectPathGen2UnsupportedReason.
        
    
    .. py:attribute:: vmotionSupported
    
        Flag indicating whether you can perform VMotion.
        
    
    .. py:attribute:: vmotionWithStorageVMotionSupported
    
        Indicates whether the storage of a powered-on virtual machine may be relocated while simultaneously changing the execution host of the virtual machine.
        
    
    .. py:attribute:: vStorageCapable
    
        Indicates whether the host supports vStorage Hardware acceleration.
        
    