
================================================================================
VirtualDeviceConnectInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_device.VirtualDevice`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.virtual_device_connect_info.VirtualDeviceConnectInfo
    
    .. py:attribute:: allowGuestControl
    
        Enables guest control over whether the connectable device is connected.
        
    
    .. py:attribute:: connected
    
        Indicates whether the device is currently connected. Valid only while the virtual machine is running.
        
    
    .. py:attribute:: startConnected
    
        Specifies whether or not to connect the device when the virtual machine starts.
        
    
    .. py:attribute:: status
    
        Indicates the current status of the connectable device. Valid only while the virtual machine is running. The set of possible values is described in VirtualDeviceConnectInfoStatus
        
    