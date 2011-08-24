
================================================================================
VirtualDiskSparseVer2BackingOption
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.bool_option.BoolOption`,
    :py:class:`~pyvisdk.do.choice_option.ChoiceOption`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_device_file_backing_option.VirtualDeviceFileBackingOption`
    
.. class:: pyvisdk.do.virtual_disk_sparse_ver2_backing_option.VirtualDiskSparseVer2BackingOption
    
    .. py:attribute:: diskMode
    
        The disk mode. Valid disk modes are: * persistent * nonpersistent * undoable * independent_persistent * independent_nonpersistent * append
        
    
    .. py:attribute:: growable
    
        Indicates whether or not this disk backing can be extended to larger sizes through a reconfigure operation.
        
    
    .. py:attribute:: hotGrowable
    
        Indicates whether or not this disk backing can be extended to larger sizes through a reconfigure operation while the virtual machine is powered on.
        
    
    .. py:attribute:: split
    
        Flag to indicate whether or not the host supports allowing the client to select whether or not a sparse disk should be split.
        
    
    .. py:attribute:: uuid
    
        Flag to indicate whether this backing supports disk UUID property.
        
    
    .. py:attribute:: writeThrough
    
        Flag to indicate whether or not the host supports allowing the client to select "writethrough" as a mode for virtual disks. Typically, this is available only for VMware Server Linux hosts.
        
    