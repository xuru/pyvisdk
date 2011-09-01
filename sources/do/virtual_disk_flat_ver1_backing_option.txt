
================================================================================
VirtualDiskFlatVer1BackingOption
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.bool_option.BoolOption`,
    :py:class:`~pyvisdk.do.choice_option.ChoiceOption`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_device_file_backing_option.VirtualDeviceFileBackingOption`
    
.. class:: pyvisdk.do.virtual_disk_flat_ver1_backing_option.VirtualDiskFlatVer1BackingOption
    
    .. py:attribute:: diskMode
    
        The disk mode. Valid disk modes are: * persistent * nonpersistent * undoable * independent_persistent * independent_nonpersistent * append See VirtualDiskMode
        
    
    .. py:attribute:: growable
    
        Flag to indicate whether this backing can have its size changed.
        
    
    .. py:attribute:: split
    
        Flag to indicate whether or not the host supports allowing the client to select whether or not a disk should be split.
        
    
    .. py:attribute:: writeThrough
    
        Flag to indicate whether or not the host supports allowing the client to select "writethrough" as a mode for virtual disks. Typically, this is available only for GSX Server Linux hosts.
        
    