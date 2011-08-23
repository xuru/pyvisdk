
================================================================================
AutoStartPowerInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_auto_start_manager_config.HostAutoStartManagerConfig`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.auto_start_wait_heartbeat_setting.AutoStartWaitHeartbeatSetting`,
    :py:class:`~pyvisdk.do.virtual_machine.VirtualMachine`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.auto_start_power_info.AutoStartPowerInfo
    
    .. py:attribute:: key
    
        Virtual machine to power on or power off.
        
    
    .. py:attribute:: startAction
    
        How to start the virtual machine. Valid settings are none or powerOn. If set to none, then the virtual machine does not participate in auto-start.
        
    
    .. py:attribute:: startDelay
    
        Delay in seconds before continuing with the next virtual machine in the order of machines to be started. If the delay is specified as -1, then the system default is used.
        
    
    .. py:attribute:: startOrder
    
        The autostart priority of this virtual machine. Virtual machines with a lower number are powered on first. On host shutdown, the virtual machines are shut down in reverse order, meaning those with a higher number are powered off first.
        
    
    .. py:attribute:: stopAction
    
        Defines the stop action for the virtual machine. Can be set to none, systemDefault, powerOff, or suspend. If set to none, then the virtual machine does not participate in auto-stop.
        
    
    .. py:attribute:: stopDelay
    
        Delay in seconds before continuing with the next virtual machine in the order sequence. If the delay is -1, then the system default is used.
        
    
    .. py:attribute:: waitForHeartbeat
    
        
        
    