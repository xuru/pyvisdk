
================================================================================
VirtualMachineScsiDiskDeviceInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.config_target.ConfigTarget`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_scsi_disk.HostScsiDisk`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_machine_disk_device_info.VirtualMachineDiskDeviceInfo`
    
.. class:: pyvisdk.do.virtual_machine_scsi_disk_device_info.VirtualMachineScsiDiskDeviceInfo
    
    .. py:attribute:: disk
    
        Detailed information about the disk.
        
    
    .. py:attribute:: lunNumber
    
        LUN number hint used to identify the SCSI device. To definitively correlate this device with a host physical disk, use the disk property. This identifier is intended as a hint to end users to identify the disk device.
        
    
    .. py:attribute:: transportHint
    
        Transport identifier hint used to identify the device. To definitively correlate this device with a host physical disk, use the disk property. This identifier is intended as a hint to end users to identify the disk device.
        
    