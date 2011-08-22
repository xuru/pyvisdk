
================================================================================
HostMultipathInfoLogicalUnit
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_multipath_info.HostMultipathInfo`,
    :py:class:`~pyvisdk.do.host_multipath_info_path.HostMultipathInfoPath`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_multipath_info_logical_unit_policy.HostMultipathInfoLogicalUnitPolicy`,
    :py:class:`~pyvisdk.do.host_multipath_info_logical_unit_storage_array_type_policy.HostMultipathInfoLogicalUnitStorageArrayTypePolicy`,
    :py:class:`~pyvisdk.do.host_multipath_info_path.HostMultipathInfoPath`,
    :py:class:`~pyvisdk.do.scsi_lun.ScsiLun`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_multipath_info_logical_unit.HostMultipathInfoLogicalUnit
    
    .. py:attribute:: id
    
        Identifier of LogicalUnit.
        
    
    .. py:attribute:: key
    
        Linkable identifier.
        
    
    .. py:attribute:: lun
    
        The SCSI device corresponding to logical unit.
        
    
    .. py:attribute:: path
    
        The array of paths available to access this LogicalUnit.
        
    
    .. py:attribute:: policy
    
        Policy that the logical unit should use when selecting a path.
        
    
    .. py:attribute:: storageArrayTypePolicy
    
        Policy used to determine how a storage device is accessed. This policy is currently immutable.
        
    