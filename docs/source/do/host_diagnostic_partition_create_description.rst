
================================================================================
HostDiagnosticPartitionCreateDescription
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_diagnostic_partition_create_spec.HostDiagnosticPartitionCreateSpec`,
    :py:class:`~pyvisdk.do.host_disk_partition_layout.HostDiskPartitionLayout`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_partition_create_desc.QueryPartitionCreateDesc`
    
.. class:: pyvisdk.do.host_diagnostic_partition_create_description.HostDiagnosticPartitionCreateDescription
    
    .. py:attribute:: diskUuid
    
        The UUID of the SCSI disk on which to create the diagnostic partition. This disk UUID will match that found in the identification field of the creation spec.See HostScsiDiskSee uuid
        
    
    .. py:attribute:: layout
    
        Layout describing the format of the disk
        
    
    .. py:attribute:: spec
    
        Creation specification for diagnostic partition
        
    