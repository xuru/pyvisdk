
================================================================================
HostVmfsVolume
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_unresolved_vmfs_resolution_result.HostUnresolvedVmfsResolutionResult`,
    :py:class:`~pyvisdk.do.vmfs_datastore_info.VmfsDatastoreInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_force_mounted_info.HostForceMountedInfo`,
    :py:class:`~pyvisdk.do.host_scsi_disk_partition.HostScsiDiskPartition`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.host_file_system_volume.HostFileSystemVolume`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.format_vmfs.FormatVmfs`
    
.. class:: pyvisdk.do.host_vmfs_volume.HostVmfsVolume
    
    .. py:attribute:: blockSizeMb
    
        Block size of VMFS. Determines maximum file size. The maximum number of blocks is typically fixed with each specific version of VMFS. To increase the maximum size of a VMFS file, increase the block size.
        
    
    .. py:attribute:: extent
    
        The list of partition names that comprise this disk's VMFS extents.
        
    
    .. py:attribute:: forceMountedInfo
    
        Information about 'forceMounted' VmfsVolume. When the system detects a copy of a VmfsVolume, it will not be auto-mounted on the host and it will be detected as 'UnresolvedVmfsVolume'. If user decides to 'forceMount' the VmfsVolume on the host, forceMountedInfo will be populated. It will not be set for automounted VMFS volumes.
        
    
    .. py:attribute:: majorVersion
    
        Major version number of VMFS.
        
    
    .. py:attribute:: maxBlocks
    
        Maximum number of blocks. Determines maximum file size along with blockSize. See information about the blockSize.
        
    
    .. py:attribute:: uuid
    
        The universally unique identifier assigned to VMFS.
        
    
    .. py:attribute:: version
    
        Version string. Contains major and minor version numbers.
        
    
    .. py:attribute:: vmfsUpgradable
    
        Can the filesystem be upgraded to a newer version.See UpgradeVmfs
        
    