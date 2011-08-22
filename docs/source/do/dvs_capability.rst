
================================================================================
DVSCapability
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.update_dvs_capability.UpdateDvsCapability`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.distributed_virtual_switch.DistributedVirtualSwitch`,
    :py:class:`~pyvisdk.do.dvs_create_spec.DVSCreateSpec`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.distributed_virtual_switch_host_product_spec.DistributedVirtualSwitchHostProductSpec`,
    :py:class:`~pyvisdk.do.dvs_feature_capability.DVSFeatureCapability`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.dvs_capability.DVSCapability
    
    .. py:attribute:: compatibleHostComponentProductInfo
    
        The list of host component product information that is compatible with the current switch implementation.
        
    
    .. py:attribute:: dvPortGroupOperationSupported
    
        Whether this switch allows vCenter users to modify DVS configuration at the portgroup level, except for host member, policy, and scope operations.
        
    
    .. py:attribute:: dvPortOperationSupported
    
        Whether this switch allows vCenter users to modify DVS configuration at the port level, except for host member, policy, and scope operations.
        
    
    .. py:attribute:: dvsOperationSupported
    
        Whether this switch allows vCenter users to modify DVS configuration at the switch level, except for host member, policy, and scope operations.
        
    
    .. py:attribute:: featuresSupported
    
        Indicators for which version-specific DVS features are available on this switch. This information is read-only; it cannot be specified when creating a DVS, and it cannot be modified by UpdateDvsCapability.
        
    