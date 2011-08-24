
================================================================================
AutoStartDefaults
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_auto_start_manager_config.HostAutoStartManagerConfig`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.auto_start_defaults.AutoStartDefaults
    
    .. py:attribute:: enabled
    
        Indicates whether or not auto-start manager is enabled.
        
    
    .. py:attribute:: startDelay
    
        System-default autoStart delay in seconds. The default is 120 seconds.
        
    
    .. py:attribute:: stopAction
    
        System-default power-off action. Used if the stopAction string in the AutoPowerInfo object for a particular machine is set to systemDefault. If stopAction and startAction for a virtual machine are both set to none, that virtual machine is removed from the AutoStart sequence.
        
    
    .. py:attribute:: stopDelay
    
        System-default autoStop delay in seconds. The default is 120 seconds.
        
    
    .. py:attribute:: waitForHeartbeat
    
        System-default waitForHeartbeat setting.
        
    