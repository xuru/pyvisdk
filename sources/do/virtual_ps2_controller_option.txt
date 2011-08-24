
================================================================================
VirtualPS2ControllerOption
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.int_option.IntOption`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_controller_option.VirtualControllerOption`
    
.. class:: pyvisdk.do.virtual_ps2_controller_option.VirtualPS2ControllerOption
    
    .. py:attribute:: numKeyboards
    
        The minimum, maximum, and default number of keyboards you can have at any given time. This is further constrained by the number of available slots in the PS/2 controller. The minimum, maximum, and default are integers defined by three properties: *
        
    
    .. py:attribute:: numPointingDevices
    
        The minimum, maximum, and default number of mice you can have at any given time. The number of mice is also limited by the number of available slots in the PS/2 controller. The minimum, maximum, and default are integers defined by three properties: *
        
    