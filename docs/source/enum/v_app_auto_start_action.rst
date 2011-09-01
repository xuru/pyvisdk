
==================================================================================================
VAppAutoStartAction
==================================================================================================

.. describe:: VAppAutoStartAction

    
    
    
    .. py:data:: VAppAutoStartAction.guestShutdown
    
        The guest operating system for a virtual machine is shut down when that virtual machine in next in the auto-stop order.
        
    
    .. py:data:: VAppAutoStartAction.none
    
        No action is taken for this virtual machine. This virtual machine is not a part of the auto-start sequence. This can be used for both auto-start and auto-start settings.
        
    
    .. py:data:: VAppAutoStartAction.powerOff
    
        This virtual machine is powered off when it is next in the auto-stop order. This is the default stopAction.
        
    
    .. py:data:: VAppAutoStartAction.powerOn
    
        This virtual machine is powered on when it is next in the auto-start order.
        
    
    .. py:data:: VAppAutoStartAction.suspend
    
        This virtual machine is suspended when it is next in the auto-stop order.
        
    