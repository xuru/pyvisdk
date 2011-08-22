
================================================================================
VirtualDiskRawDiskMappingVer1BackingOption
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.choice_option.ChoiceOption`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_device_device_backing_option.VirtualDeviceDeviceBackingOption`
    
.. class:: pyvisdk.do.virtual_disk_raw_disk_mapping_ver1_backing_option.VirtualDiskRawDiskMappingVer1BackingOption
    
    .. py:attribute:: compatibilityMode
    
        The supported raw disk mapping compatibility modes.
        
    
    .. py:attribute:: descriptorFileNameExtensions
    
        Valid extensions for the filename of the optional raw disk mapping descriptor file. This is present only for ESX Server 3.x and greater hosts.
        
    
    .. py:attribute:: diskMode
    
        The disk mode. Valid values are: * persistent * independent_persistent * independent_nonpersistent
        
    
    .. py:attribute:: uuid
    
        Flag to indicate whether this backing supports disk UUID property.
        
    