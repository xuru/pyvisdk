
================================================================================
HostAutoStartManagerConfig
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.reconfigure_autostart.ReconfigureAutostart`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_auto_start_manager.HostAutoStartManager`,
    :py:class:`~pyvisdk.do.host_config_info.HostConfigInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.auto_start_defaults.AutoStartDefaults`,
    :py:class:`~pyvisdk.do.auto_start_power_info.AutoStartPowerInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_auto_start_manager_config.HostAutoStartManagerConfig
    
    .. py:attribute:: defaults
    
        System defaults for auto-start/auto-stop.
        
    
    .. py:attribute:: powerInfo
    
        Lists the auto-start/auto-stop configuration. If a virtual machine is not mentioned in this array, it does not participate in auto-start/auto-stop operations.
        
    