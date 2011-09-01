
================================================================================
VirtualEthernetCard
================================================================================


.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.virtual_e1000.VirtualE1000`,
    :py:class:`~pyvisdk.do.virtual_pc_net32.VirtualPCNet32`,
    :py:class:`~pyvisdk.do.virtual_vmxnet.VirtualVmxnet`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_device.VirtualDevice`
    
.. class:: pyvisdk.do.virtual_ethernet_card.VirtualEthernetCard
    
    .. py:attribute:: addressType
    
        MAC address type.
        
    
    .. py:attribute:: macAddress
    
        MAC address assigned to the virtual network adapter. Clients can set this property to any of the allowed address types. The server might override the specified value for "Generated" or "Assigned" if it does not fall in the right ranges or is determined to be a duplicate.
        
    
    .. py:attribute:: wakeOnLanEnabled
    
        Indicates whether wake-on-LAN is enabled on this virtual network adapter. Clients can set this property to selectively enable or disable wake-on-LAN.
        
    