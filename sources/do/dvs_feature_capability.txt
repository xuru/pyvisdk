
================================================================================
DVSFeatureCapability
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.dvs_capability.DVSCapability`
    
.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.v_mware_dvs_feature_capability.VMwareDVSFeatureCapability`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_dvs_feature_capability.QueryDvsFeatureCapability`
    
.. class:: pyvisdk.do.dvs_feature_capability.DVSFeatureCapability
    
    .. py:attribute:: networkResourceManagementSupported
    
        Flag to indicate whether network I/O control is supported on the vNetwork Distributed Switch.
        
    
    .. py:attribute:: networkResourcePoolHighShareValue
    
        This is the value for high in shares. This implicitly defines the legal range of share values to be between 1 and this. This also defines values for other level types, such as normal being one half of this value and low being one fourth of this value.
        
    
    .. py:attribute:: nicTeamingPolicy
    
        The available teaming modes for the vNetwork Distributed Switch. The value can be one or more of DistributedVirtualSwitchNicTeamingPolicyMode.
        
    
    .. py:attribute:: vmDirectPathGen2Supported
    
        Flag to indicate whether VMDirectPath Gen 2 is supported on the vNetwork Distributed Switch.
        
    