
================================================================================
OvfParseDescriptorResult
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.key_value.KeyValue`,
    :py:class:`~pyvisdk.do.localized_method_fault.LocalizedMethodFault`,
    :py:class:`~pyvisdk.do.ovf_deployment_option.OvfDeploymentOption`,
    :py:class:`~pyvisdk.do.ovf_network_info.OvfNetworkInfo`,
    :py:class:`~pyvisdk.do.v_app_product_info.VAppProductInfo`,
    :py:class:`~pyvisdk.do.v_app_property_info.VAppPropertyInfo`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.parse_descriptor.ParseDescriptor`
    
.. class:: pyvisdk.do.ovf_parse_descriptor_result.OvfParseDescriptorResult
    
    .. py:attribute:: annotation
    
        The annotation info contained in the OVF
        
    
    .. py:attribute:: approximateDownloadSize
    
        The OVF Manager's best guess as to the total amount of data that must be transferred to download the entity.
        
    
    .. py:attribute:: approximateFlatDeploymentSize
    
        The OVF Manager's best guess as to the total amount of space required to deploy the entity if using flat disks.
        
    
    .. py:attribute:: approximateSparseDeploymentSize
    
        The OVF Manager's best guess as to the total amount of space required to deploy the entity using sparse disks.
        
    
    .. py:attribute:: defaultDeploymentOption
    
        The key of the default deployment option. Empty only if there are no deployment options.
        
    
    .. py:attribute:: defaultEntityName
    
        The default name to use for the entity, if a product name is not specified. This is the ID of the OVF top-level entity, or taken from a ProductSection.
        
    
    .. py:attribute:: deploymentOption
    
        The list of possible deployment options.
        
    
    .. py:attribute:: entityName
    
        A list of the child entities contained in this package and their location in the vApp hierarchy. Each entry is a (key,value) pair, where the key is the display name, and the value is a unique path identifier for the entity in the vApp. The path is constructed by appending the id of each entity of the path down to the entity, separated by slashes. For example, the path for a child of the root entity with id = "vm1", would simply be "vm1". If the vm is the child of a VirtualSystemCollection called "webTier", then the path would be "webTier/vm".
        
    
    .. py:attribute:: error
    
        Errors that happened during processing. Something will be wrong with the result.
        
    
    .. py:attribute:: eula
    
        The list of all EULAs contained in the OVF
        
    
    .. py:attribute:: ipAllocationScheme
    
        The kind of IP allocation supported by the guest.
        
    
    .. py:attribute:: ipProtocols
    
        The IP protocols supported by the guest.
        
    
    .. py:attribute:: network
    
        The list of networks required by the OVF
        
    
    .. py:attribute:: productInfo
    
        The product info contained in the OVF
        
    
    .. py:attribute:: property_
    
        Metadata about the properties contained in the OVF
        
    
    .. py:attribute:: virtualApp
    
        True if the OVF contains a vApp (containing one or more vApps and/or virtual machines), as opposed to a single virtual machine.
        
    
    .. py:attribute:: warning
    
        Non-fatal warnings from the processing. The result will be valid, but the user may choose to reject it based on these warnings.
        
    