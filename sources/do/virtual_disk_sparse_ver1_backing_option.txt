
================================================================================
VirtualDiskSparseVer1BackingOption
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.bool_option.BoolOption`,
    :py:class:`~pyvisdk.do.choice_option.ChoiceOption`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_device_file_backing_option.VirtualDeviceFileBackingOption`
    
.. class:: pyvisdk.do.virtual_disk_sparse_ver1_backing_option.VirtualDiskSparseVer1BackingOption
    
    .. py:attribute:: diskModes
    
        The disk mode. Valid disk modes are: * persistent * nonpersistent * undoable * independent_persistent * independent_nonpersistent * append See VirtualDiskMode
        
    
    .. py:attribute:: growable
    
        Flag to indicate whether this backing can have its size changed.
        
    
    .. py:attribute:: split
    
        Flag to indicate whether or not the host supports allowing the client to select whether or not a sparse disk should be split.
        
    
    .. py:attribute:: writeThrough
    
        Flag to indicate whether or not the host supports allowing the client to select "writethrough" as a mode for virtual disks. Typically, this is available only for VMware Server Linux hosts.
        
    