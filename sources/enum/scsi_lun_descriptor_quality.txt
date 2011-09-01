
==================================================================================================
ScsiLunDescriptorQuality
==================================================================================================

.. describe:: ScsiLunDescriptorQuality

    An indicator of the utility of Descriptor in being used as an identifier that is stable, unique, and correlatable.
    
    
    .. py:data:: ScsiLunDescriptorQuality.highQuality
    
        The Descriptor has an identifier that is useful for identification and correlation across hosts.
        
    
    .. py:data:: ScsiLunDescriptorQuality.lowQuality
    
        The Descriptor has an identifier that should not be used for identification and correlation across hosts.
        
    
    .. py:data:: ScsiLunDescriptorQuality.mediumQuality
    
        The Descriptor has an identifier that may be used for identification and correlation across hosts.
        
    
    .. py:data:: ScsiLunDescriptorQuality.unknownQuality
    
        The Descriptor has an identifier that may or may not be useful for identification and correlation across hosts.
        
    