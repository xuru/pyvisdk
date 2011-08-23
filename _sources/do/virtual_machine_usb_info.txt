
================================================================================
VirtualMachineUsbInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.config_target.ConfigTarget`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.virtual_machine_summary.VirtualMachineSummary`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_machine_target_info.VirtualMachineTargetInfo`
    
.. class:: pyvisdk.do.virtual_machine_usb_info.VirtualMachineUsbInfo
    
    .. py:attribute:: description
    
        A user visible name of the USB device.
        
    
    .. py:attribute:: family
    
        The device class families. For possible values see VirtualMachineUsbInfoFamily
        
    
    .. py:attribute:: physicalPath
    
        An autoconnect pattern which describes the device's physical path. This is the path to the specific port on the host where the USB device is attached.
        
    
    .. py:attribute:: product
    
        The product ID of the USB device.
        
    
    .. py:attribute:: speed
    
        The possible device speeds detected by server. For possible values see VirtualMachineUsbInfoSpeed
        
    
    .. py:attribute:: summary
    
        Summary information about the virtual machine that is currently using this device, if any.
        
    
    .. py:attribute:: vendor
    
        The vendor ID of the USB device.
        
    