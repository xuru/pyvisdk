
================================================================================
HostMultipathInfoPath
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_multipath_info_logical_unit.HostMultipathInfoLogicalUnit`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_host_bus_adapter.HostHostBusAdapter`,
    :py:class:`~pyvisdk.do.host_multipath_info_logical_unit.HostMultipathInfoLogicalUnit`,
    :py:class:`~pyvisdk.do.host_target_transport.HostTargetTransport`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_multipath_info_path.HostMultipathInfoPath
    
    .. py:attribute:: adapter
    
        The host bus adapter at one endpoint of this path.
        
    
    .. py:attribute:: isWorkingPath
    
        A path, managed by a given path selection policy(psp) plugin, is denoted to be a Working Path if the psp plugin is likely to select the path for performing I/O in the near future.
        
    
    .. py:attribute:: key
    
        The identifier of the Path.
        
    
    .. py:attribute:: lun
    
        The logical unit at one endpoint of this path.
        
    
    .. py:attribute:: name
    
        Name of path.
        
    
    .. py:attribute:: pathState
    
        *
        
    
    .. py:attribute:: state
    
        The system reported state of the path. Must be one of the values of MultipathState
        
    
    .. py:attribute:: transport
    
        Transport information for the target end of the path.
        
    