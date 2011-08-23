
================================================================================
HostVmfsSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.format_vmfs.FormatVmfs`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.vmfs_datastore_create_spec.VmfsDatastoreCreateSpec`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_scsi_disk_partition.HostScsiDiskPartition`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_vmfs_spec.HostVmfsSpec
    
    .. py:attribute:: blockSizeMb
    
        The block size of VMFS in megabytes (MB). Determines the maximum file size. If this optional property is not set, the maximum file size defaults to the maximum file size for the platform.
        
    
    .. py:attribute:: extent
    
        Head extent of VMFS. The head extent identifies the VMFS. However, the head extent should not be used to identify the VMFS across host reboots. The actual identifier is specified in "vmhbaI:T:L" format which is not guaranteed to be stable across reboots. Define a volume name that is unique to the host and use it to refer to the VMFS. Alternatively, the immutable UUID of the VMFS can be used after it is created.
        
    
    .. py:attribute:: majorVersion
    
        Major version number of VMFS. This can be changed if the VMFS is upgraded, but this is an irreversible change.
        
    
    .. py:attribute:: volumeName
    
        Volume name of VMFS.
        
    