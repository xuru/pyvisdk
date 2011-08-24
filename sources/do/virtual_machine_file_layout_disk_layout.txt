
================================================================================
VirtualMachineFileLayoutDiskLayout
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_machine_file_layout.VirtualMachineFileLayout`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.virtual_machine_file_layout_disk_layout.VirtualMachineFileLayoutDiskLayout
    
    .. py:attribute:: diskFile
    
        List of files that makes up the virtual disk. At least one entry always exists in this array. The first entry is the main descriptor of the virtual disk (the one used when adding the disk to a virtual machine). These are complete datastore paths, not relative paths.
        
    
    .. py:attribute:: key
    
        Identification of the disk in config.
        
    