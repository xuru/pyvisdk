
==================================================================================================
VirtualDeviceConnectInfoStatus
==================================================================================================

.. describe:: VirtualDeviceConnectInfoStatus

    Specifies the connectable virtual device status.
    
    
    .. py:data:: VirtualDeviceConnectInfoStatus.ok
    
        The device is working correctly.
        
    
    .. py:data:: VirtualDeviceConnectInfoStatus.recoverableError
    
        The device has reported a recoverable error. For example, attempting to connect to floppy device that is being used by another virtual machine or some other program would result in this status.
        
    
    .. py:data:: VirtualDeviceConnectInfoStatus.unrecoverableError
    
        The device cannot be used. For example, attempting to connect to a floppy device that does not exist would result in this status.
        
    
    .. py:data:: VirtualDeviceConnectInfoStatus.untried
    
        The device status is unknown, or it has not been requested to connect when the VM is powered on.
        
    