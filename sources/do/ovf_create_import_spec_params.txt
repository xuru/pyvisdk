
================================================================================
OvfCreateImportSpecParams
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.create_import_spec.CreateImportSpec`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_system.HostSystem`,
    :py:class:`~pyvisdk.do.key_value.KeyValue`,
    :py:class:`~pyvisdk.do.ovf_network_mapping.OvfNetworkMapping`,
    :py:class:`~pyvisdk.do.ovf_resource_map.OvfResourceMap`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.ovf_manager_common_params.OvfManagerCommonParams`
    
.. class:: pyvisdk.do.ovf_create_import_spec_params.OvfCreateImportSpecParams
    
    .. py:attribute:: diskProvisioning
    
        An optional disk provisioning. If set, all the disks in the deployed OVF will have get the same specified disk type (e.g., thin provisioned). The valide values for disk provisioning are: * monolithicSparse * monolithicFlat * twoGbMaxExtentSparse * twoGbMaxExtentFlat * thin * thick * sparse * flat
        
    
    .. py:attribute:: entityName
    
        The name to set on the entity (more precisely, on the top-level vApp or VM of the entity) as it appears in VI. If empty, the product name is obtained from the ProductSection of the descriptor. If that name is not specified, the ovf:id of the top-level entity is used.
        
    
    .. py:attribute:: hostSystem
    
        The host to validate the OVF descriptor against, if it cannot be deduced from the resource pool.
        
    
    .. py:attribute:: ipAllocationPolicy
    
        The IP allocation policy chosen by the caller.
        
    
    .. py:attribute:: ipProtocol
    
        The IP protocol chosen by the caller.
        
    
    .. py:attribute:: networkMapping
    
        The mapping of network identifiers from the descriptor to networks in the VI infrastructure.
        
    
    .. py:attribute:: propertyMapping
    
        The assignment of values to the properties found in the descriptor. If no value is specified for an option, the default value from the descriptor is used.
        
    
    .. py:attribute:: resourceMapping
    
        The resource configuration for the created vApp. This can be used to distribute a vApp across multiple resource pools (and create linked children).
        
    