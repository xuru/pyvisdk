
================================================================================
VirtualMachineFileInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_machine_config_info.VirtualMachineConfigInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_config_spec.VirtualMachineConfigSpec`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.virtual_machine_file_info.VirtualMachineFileInfo
    
    .. py:attribute:: logDirectory
    
        Directory to store the log files for the virtual machine. If not specified, this defaults to the same directory as the configuration file,
        
    
    .. py:attribute:: snapshotDirectory
    
        Path name of the directory that typically holds suspend, redo, or snapshot files belonging to the virtual machine. This path name defaults to the same directory as the configuration file.
        
    
    .. py:attribute:: suspendDirectory
    
        Some products allow the suspend directory to be different than the snapshot directory. On products where this is not possible, setting of this property is ignored.
        
    
    .. py:attribute:: vmPathName
    
        Path name to the configuration file for the virtual machine, e.g., the .vmx file. This also implicitly defines the configuration directory.
        
    