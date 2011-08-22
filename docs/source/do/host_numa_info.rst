
================================================================================
HostNumaInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_hardware_info.HostHardwareInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_numa_node.HostNumaNode`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_numa_info.HostNumaInfo
    
    .. py:attribute:: numaNode
    
        Information about each of the NUMA nodes on the host. The array is empty if the host is not NUMA-capable.
        
    
    .. py:attribute:: numNodes
    
        The number of NUMA nodes on the host. The value is 0 if the host is not NUMA-capable.
        
    
    .. py:attribute:: type
    
        The type of the NUMA. Currently there is only one value: "X440".
        
    