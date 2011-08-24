
================================================================================
DVSPolicy
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.dvs_config_info.DVSConfigInfo`,
    :py:class:`~pyvisdk.do.dvs_config_spec.DVSConfigSpec`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.dvs_policy.DVSPolicy
    
    .. py:attribute:: autoPreInstallAllowed
    
        Whether downloading a new proxy VirtualSwitch module to the host is allowed to be automatically executed by the switch.
        
    
    .. py:attribute:: autoUpgradeAllowed
    
        Whether upgrading of the switch is allowed to be automatically executed by the switch.
        
    
    .. py:attribute:: partialUpgradeAllowed
    
        Whether to allow upgrading a switch when some of the hosts failed to install the needed module. The vCenter Server will reattempt the pre-install operation of the host module on those failed hosts, whenever they reconnect to vCenter.
        
    