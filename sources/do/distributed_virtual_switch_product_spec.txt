
================================================================================
DistributedVirtualSwitchProductSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.perform_dvs_product_spec_operation__task.PerformDvsProductSpecOperation_Task`,
    :py:meth:`~pyvisdk.do.query_compatible_host_for_new_dvs.QueryCompatibleHostForNewDvs`,
    :py:meth:`~pyvisdk.do.query_dvs_compatible_host_spec.QueryDvsCompatibleHostSpec`,
    :py:meth:`~pyvisdk.do.query_dvs_feature_capability.QueryDvsFeatureCapability`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.distributed_virtual_switch_host_member.DistributedVirtualSwitchHostMember`,
    :py:class:`~pyvisdk.do.distributed_virtual_switch_manager_dvs_product_spec.DistributedVirtualSwitchManagerDvsProductSpec`,
    :py:class:`~pyvisdk.do.dvs_config_info.DVSConfigInfo`,
    :py:class:`~pyvisdk.do.dvs_create_spec.DVSCreateSpec`,
    :py:class:`~pyvisdk.do.dvs_summary.DVSSummary`,
    :py:class:`~pyvisdk.do.dvs_upgrade_available_event.DvsUpgradeAvailableEvent`,
    :py:class:`~pyvisdk.do.dvs_upgraded_event.DvsUpgradedEvent`,
    :py:class:`~pyvisdk.do.dvs_upgrade_in_progress_event.DvsUpgradeInProgressEvent`,
    :py:class:`~pyvisdk.do.dvs_upgrade_rejected_event.DvsUpgradeRejectedEvent`,
    :py:class:`~pyvisdk.do.not_supported_host_in_dvs.NotSupportedHostInDvs`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_available_dvs_spec.QueryAvailableDvsSpec`
    
.. class:: pyvisdk.do.distributed_virtual_switch_product_spec.DistributedVirtualSwitchProductSpec
    
    .. py:attribute:: build
    
        Build string for the server on which this call is made. For example, x.y.z-num. This string does not apply to the API.
        
    
    .. py:attribute:: bundleId
    
        The ID of the bundle if a host component bundle needs to be installed on the host members to support the functionality of the switch.
        
    
    .. py:attribute:: bundleUrl
    
        The URL of the bundle that VMware Update Manager will use to install the bundle on the host members, if bundleId is set.
        
    
    .. py:attribute:: forwardingClass
    
        Forwarding class of the distributed virtual switch.
        
    
    .. py:attribute:: name
    
        Short form of the product name.
        
    
    .. py:attribute:: vendor
    
        Name of the vendor of this product.
        
    
    .. py:attribute:: version
    
        Dot-separated version string. For example, "1.2".
        
    