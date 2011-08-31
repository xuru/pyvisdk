
================================================================================
HostDiagnosticPartitionCreateSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.create_diagnostic_partition.CreateDiagnosticPartition`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_diagnostic_partition_create_description.HostDiagnosticPartitionCreateDescription`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_disk_partition_spec.HostDiskPartitionSpec`,
    :py:class:`~pyvisdk.do.host_scsi_disk_partition.HostScsiDiskPartition`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_diagnostic_partition_create_spec.HostDiagnosticPartitionCreateSpec
    
    .. py:attribute:: active
    
        Indicates if the created diagnostic partition should be made the active diagnostic partition. If not supplied, the system will decide whether or not the created specification is active.
        
    
    .. py:attribute:: diagnosticType
    
        Indicates the type of the diagnostic partition to be created.See DiagnosticPartitionType
        
    
    .. py:attribute:: id
    
        Diagnostic partition identification information.
        
    
    .. py:attribute:: partition
    
        Partitioning specification.
        
    
    .. py:attribute:: storageType
    
        Indicates the storage type where the diagnostic partition will be created.See DiagnosticPartitionStorageType
        
    