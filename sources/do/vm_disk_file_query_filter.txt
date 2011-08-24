
================================================================================
VmDiskFileQueryFilter
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.vm_disk_file_query.VmDiskFileQuery`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.vm_disk_file_query_filter.VmDiskFileQueryFilter
    
    .. py:attribute:: controllerType
    
        If this optional property is set, only virtual disk files that have a controller type that matches one of the controller types specified are returned. If no controller types are specified, this search criteria is ignored.
        
    
    .. py:attribute:: diskType
    
        If this optional property is set, only the virtual disk primary files that match one of the specified disk types are selected. If no disk types are specified, this search criteria is ignored.
        
    
    .. py:attribute:: matchHardwareVersion
    
        If this optional property is set, only virtual disk primary files that match one of the specified hardware versions are selected. If no versions are specified, this search criteria is ignored.
        
    
    .. py:attribute:: thin
    
        This optional property can be used to filter disks based on whether they are thin-provsioned or not: if set to true, only thin-provisioned disks are returned, and vice-versa.
        
    