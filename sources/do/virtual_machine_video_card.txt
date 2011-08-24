
================================================================================
VirtualMachineVideoCard
================================================================================


.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_device.VirtualDevice`
    
.. class:: pyvisdk.do.virtual_machine_video_card.VirtualMachineVideoCard
    
    .. py:attribute:: enable3DSupport
    
        Flag to indicate whether the virtual video card supports 3D functions. This property can only be updated when the virtual machine is powered off.
        
    
    .. py:attribute:: numDisplays
    
        Indicates the number of supported monitors. The number of displays X the maximum resolution of each display is bounded by the video RAM size of the virtual video card. This property can only be updated when the virtual machine is powered off.
        
    
    .. py:attribute:: useAutoDetect
    
        Flag to indicate whether the display settings of the host on which the virtual machine is running should be used to automatically determine the display settings of the virtual machine's video card. This setting takes effect at virtual machine power-on time. If this value is set to TRUE, numDisplays will be ignored.
        
    
    .. py:attribute:: videoRamSizeInKB
    
        The size of the framebuffer for a virtual machine.
        
    