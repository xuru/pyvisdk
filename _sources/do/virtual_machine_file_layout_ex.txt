
================================================================================
VirtualMachineFileLayoutEx
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_machine.VirtualMachine`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.virtual_machine_file_layout_ex_disk_layout.VirtualMachineFileLayoutExDiskLayout`,
    :py:class:`~pyvisdk.do.virtual_machine_file_layout_ex_file_info.VirtualMachineFileLayoutExFileInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_file_layout_ex_snapshot_layout.VirtualMachineFileLayoutExSnapshotLayout`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.virtual_machine_file_layout_ex.VirtualMachineFileLayoutEx
    
    .. py:attribute:: disk
    
        Layout of each virtual disk attached to the virtual machine.
        
    
    .. py:attribute:: file
    
        Information about all the files that constitute the virtual machine including configuration files, disks, swap file, suspend file, log files, core files, memory file etc. VirtualMachineFileLayoutExFileType lists the different file-types that make a virtual machine.
        
    
    .. py:attribute:: snapshot
    
        Layout of each snapshot of the virtual machine.
        
    
    .. py:attribute:: timestamp
    
        Time when values in this structure were last updated.
        
    