
==================================================================================================
VirtualDiskCompatibilityMode
==================================================================================================

.. describe:: VirtualDiskCompatibilityMode

    All known compatibility modes for raw disk mappings. Valid compatibility modes are:* virtualMode * physicalMode
    
    
    .. py:data:: VirtualDiskCompatibilityMode.physicalMode
    
        A disk device backed by a physical compatibility mode raw disk mapping cannot use disk modes, and commands are passed straight through to the LUN indicated by the raw disk mapping.
        
    
    .. py:data:: VirtualDiskCompatibilityMode.virtualMode
    
        A disk device backed by a virtual compatibility mode raw disk mapping can use disk modes.See VirtualDiskMode
        
    