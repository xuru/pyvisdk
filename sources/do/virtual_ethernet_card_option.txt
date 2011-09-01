
================================================================================
VirtualEthernetCardOption
================================================================================


.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.virtual_e1000_option.VirtualE1000Option`,
    :py:class:`~pyvisdk.do.virtual_pc_net32_option.VirtualPCNet32Option`,
    :py:class:`~pyvisdk.do.virtual_vmxnet_option.VirtualVmxnetOption`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.bool_option.BoolOption`,
    :py:class:`~pyvisdk.do.choice_option.ChoiceOption`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_device_option.VirtualDeviceOption`
    
.. class:: pyvisdk.do.virtual_ethernet_card_option.VirtualEthernetCardOption
    
    .. py:attribute:: macType
    
        The supported MAC address types.
        
    
    .. py:attribute:: supportedOUI
    
        The valid Organizational Unique Identifiers (OUIs) supported by this virtual Ethernet card.
        
    
    .. py:attribute:: vmDirectPathGen2Supported
    
        Flag to indicate whether VMDirectPath Gen 2 is available on this device.
        
    
    .. py:attribute:: wakeOnLanEnabled
    
        Flag to indicate whether or not wake-on-LAN is settable on this device.
        
    