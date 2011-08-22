
================================================================================
HostCpuPackage
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_hardware_info.HostHardwareInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_cpu_id_info.HostCpuIdInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_cpu_package.HostCpuPackage
    
    .. py:attribute:: busHz
    
        Bus speed in HZ.
        
    
    .. py:attribute:: cpuFeature
    
        The CPU feature bit on this particular CPU. This is independent of the product and licensing capabilities.
        
    
    .. py:attribute:: description
    
        String summary description of CPU (for display purposes).
        
    
    .. py:attribute:: hz
    
        CPU speed in HZ.
        
    
    .. py:attribute:: index
    
        Package index, starting from zero.
        
    
    .. py:attribute:: threadId
    
        The logical CPU threads on this package.
        
    
    .. py:attribute:: vendor
    
        CPU vendor name, possible names currently are "Intel", "AMD", or "unknown".
        
    