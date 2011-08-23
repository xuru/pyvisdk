
================================================================================
HostPowerPolicy
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.power_system_capability.PowerSystemCapability`,
    :py:class:`~pyvisdk.do.power_system_info.PowerSystemInfo`
    
.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_power_policy.HostPowerPolicy
    
    .. py:attribute:: description
    
        Power Policy Description.
        
    
    .. py:attribute:: key
    
        Power Policy Key. Internally generated key which uniquely identifies power management policy on a host.
        
    
    .. py:attribute:: name
    
        Power Policy Name.
        
    
    .. py:attribute:: shortName
    
        Power Policy Short Name. This is not localizable property which can be used to identify specific power managing policies like "custom" power policy. Custom power policy has short name set to "custom".
        
    