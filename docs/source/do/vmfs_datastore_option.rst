
================================================================================
VmfsDatastoreOption
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.vmfs_datastore_base_option.VmfsDatastoreBaseOption`,
    :py:class:`~pyvisdk.do.vmfs_datastore_spec.VmfsDatastoreSpec`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_vmfs_datastore_create_options.QueryVmfsDatastoreCreateOptions`,
    :py:meth:`~pyvisdk.do.query_vmfs_datastore_expand_options.QueryVmfsDatastoreExpandOptions`,
    :py:meth:`~pyvisdk.do.query_vmfs_datastore_extend_options.QueryVmfsDatastoreExtendOptions`
    
.. class:: pyvisdk.do.vmfs_datastore_option.VmfsDatastoreOption
    
    .. py:attribute:: info
    
        Information about this VMFS datastore provisioniing option. This structure describes the extent allocation policy represented by this option.
        
    
    .. py:attribute:: spec
    
        Specification to create or increase the capacity of a VMFS datastore. This property contains a configuration specification that can be applied to effect the creation or capacity increase.
        
    