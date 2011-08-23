
================================================================================
VirtualSerialPortPipeBackingInfo
================================================================================


.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_device_pipe_backing_info.VirtualDevicePipeBackingInfo`
    
.. class:: pyvisdk.do.virtual_serial_port_pipe_backing_info.VirtualSerialPortPipeBackingInfo
    
    .. py:attribute:: endpoint
    
        Indicates the role the virtual machine assumes as an endpoint for the pipe. The valid values are "client" or "server".
        
    
    .. py:attribute:: noRxLoss
    
        Enables optimized data transfer over the pipe. When you use this feature, the ESX server buffers data to prevent data overrun. This allows the virtual machine to read all of the data transferred over the pipe with no data loss. To use optimized data transfer, set
        
    