
==================================================================================================
FileSystemMountInfoVStorageSupportStatus
==================================================================================================

.. describe:: FileSystemMountInfoVStorageSupportStatus

    Status of volume's support for vStorage hardware acceleration. The ESX Server determines the status based on the capabilities of the devices that support the file system volume. When a host boots, the support status is unknown. As the ESX host attempts hardware-accelerated operations, it determines whether the storage device supports hardware acceleration and sets the vStorageSupport property accordingly.
    
    
    .. py:data:: FileSystemMountInfoVStorageSupportStatus.vStorageSupported
    
        Storage device supports hardware acceleration. The ESX host will use the feature to offload certain storage-related operations to the device.
        
    
    .. py:data:: FileSystemMountInfoVStorageSupportStatus.vStorageUnknown
    
        Initial support status value.
        
    
    .. py:data:: FileSystemMountInfoVStorageSupportStatus.vStorageUnsupported
    
        Storage device does not support hardware acceleration. The ESX host will handle all storage-related operations.
        
    