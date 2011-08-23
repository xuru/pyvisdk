
================================================================================
HostHardwareSummary
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_list_summary.HostListSummary`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_system_identification_info.HostSystemIdentificationInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_hardware_summary.HostHardwareSummary
    
    .. py:attribute:: cpuMhz
    
        The speed of the CPU cores. This is an average value if there are multiple speeds. The product of cpuMhz and numCpuCores is approximately equal to the sum of the MHz for all the individual cores on the host.
        
    
    .. py:attribute:: cpuModel
    
        The CPU model.
        
    
    .. py:attribute:: memorySize
    
        The physical memory size in bytes.
        
    
    .. py:attribute:: model
    
        The system model identification.
        
    
    .. py:attribute:: numCpuCores
    
        Number of physical CPU cores on the host. Physical CPU cores are the processors contained by a CPU package.
        
    
    .. py:attribute:: numCpuPkgs
    
        Number of physical CPU packages on the host. Physical CPU packages are chips that contain one or more processors. Processors contained by a package are also known as CPU cores. For example, one dual-core package is comprised of one chip that contains two CPU cores.
        
    
    .. py:attribute:: numCpuThreads
    
        Number of physical CPU threads on the host.
        
    
    .. py:attribute:: numHBAs
    
        The number of host bus adapters (HBAs).
        
    
    .. py:attribute:: numNics
    
        The number of network adapters.
        
    
    .. py:attribute:: otherIdentifyingInfo
    
        Other identification information. This information may be vendor specific.
        
    
    .. py:attribute:: uuid
    
        The hardware BIOS identification.
        
    
    .. py:attribute:: vendor
    
        The hardware vendor identification.
        
    