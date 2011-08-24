
================================================================================
HostHardwareInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_system.HostSystem`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_bios_info.HostBIOSInfo`,
    :py:class:`~pyvisdk.do.host_cpu_id_info.HostCpuIdInfo`,
    :py:class:`~pyvisdk.do.host_cpu_info.HostCpuInfo`,
    :py:class:`~pyvisdk.do.host_cpu_package.HostCpuPackage`,
    :py:class:`~pyvisdk.do.host_cpu_power_management_info.HostCpuPowerManagementInfo`,
    :py:class:`~pyvisdk.do.host_numa_info.HostNumaInfo`,
    :py:class:`~pyvisdk.do.host_pci_device.HostPciDevice`,
    :py:class:`~pyvisdk.do.host_system_info.HostSystemInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_hardware_info.HostHardwareInfo
    
    .. py:attribute:: biosInfo
    
        Information about the system BIOS
        
    
    .. py:attribute:: cpuFeature
    
        CPU feature set that is supported by the hardware. This is the intersection of the feature sets supported by the individual CPU packages. This feature set is modified by the supportedCpuFeature array in the host capabilities to obtain the feature set supported by the virtualization platform.
        
    
    .. py:attribute:: cpuInfo
    
        Overall CPU information.
        
    
    .. py:attribute:: cpuPkg
    
        Information about each of the physical CPU packages on the host.
        
    
    .. py:attribute:: cpuPowerManagementInfo
    
        vSphere API 4.0
        
    
    .. py:attribute:: memorySize
    
        Total amount of physical memory on the host in bytes.
        
    
    .. py:attribute:: numaInfo
    
        Information about the NUMA (non-uniform memory access).
        
    
    .. py:attribute:: pciDevice
    
        The list of Peripheral Component Interconnect (PCI) devices available on this host.
        
    
    .. py:attribute:: systemInfo
    
        Information about the system as a whole.
        
    