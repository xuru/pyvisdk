
================================================================================
HostCpuInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_hardware_info.HostHardwareInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_cpu_info.HostCpuInfo
    
    .. py:attribute:: hz
    
        CPU speed per core. This might be an averaged value if the speed is not uniform across all cores. The total CPU speed of the box is defined as hz * numCpuCores
        
    
    .. py:attribute:: numCpuCores
    
        Number of physical CPU cores on the host.
        
    
    .. py:attribute:: numCpuPackages
    
        Number of physical CPU packages on the host.
        
    
    .. py:attribute:: numCpuThreads
    
        Number of physical CPU threads on the host.
        
    