
================================================================================
DiskChangeInfo
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.disk_change_extent.DiskChangeExtent`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_changed_disk_areas.QueryChangedDiskAreas`
    
.. class:: pyvisdk.do.disk_change_info.DiskChangeInfo
    
    .. py:attribute:: changedArea
    
        Modified disk areas. Might be empty if no parts of the disk between startOffset and startOffset + length were modified.
        
    
    .. py:attribute:: length
    
        Length (in bytes) of disk area described by this data structure.
        
    
    .. py:attribute:: startOffset
    
        Start offset (in bytes) of disk area described by this data structure.
        
    