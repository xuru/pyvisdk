
================================================================================
VirtualMachineFileLayout
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_machine.VirtualMachine`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.virtual_machine_file_layout_disk_layout.VirtualMachineFileLayoutDiskLayout`,
    :py:class:`~pyvisdk.do.virtual_machine_file_layout_snapshot_layout.VirtualMachineFileLayoutSnapshotLayout`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.virtual_machine_file_layout.VirtualMachineFileLayout
    
    .. py:attribute:: configFile
    
        A list of files that makes up the configuration of the virtual machine (excluding the .vmx file, since that file is represented in the FileInfo). These are relative paths from the configuration directory. A slash is always used as a separator. This list will typically include the NVRAM file, but could also include other meta-data files.
        
    
    .. py:attribute:: disk
    
        Files making up each virtual disk.
        
    
    .. py:attribute:: logFile
    
        A list of files stored in the virtual machine's log directory. These are relative paths from the logDirectory. A slash is always used as a separator.
        
    
    .. py:attribute:: snapshot
    
        Files of each snapshot.
        
    
    .. py:attribute:: swapFile
    
        The swapfile specific to this virtual machine, if any. This is a complete datastore path, not a relative path.
        
    