
================================================================================
HostBootDeviceInfo
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_boot_device.HostBootDevice`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_boot_devices.QueryBootDevices`
    
.. class:: pyvisdk.do.host_boot_device_info.HostBootDeviceInfo
    
    .. py:attribute:: bootDevices
    
        The list of boot devices present on the host
        
    
    .. py:attribute:: currentBootDeviceKey
    
        The key of the current boot device that the host is configured to boot. This property is unset if the current boot device is disabled.
        
    