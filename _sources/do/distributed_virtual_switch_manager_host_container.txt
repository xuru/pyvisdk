
================================================================================
DistributedVirtualSwitchManagerHostContainer
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.query_dvs_check_compatibility.QueryDvsCheckCompatibility`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.distributed_virtual_switch_manager_host_container_filter.DistributedVirtualSwitchManagerHostContainerFilter`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.managed_entity.ManagedEntity`
    
.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.distributed_virtual_switch_manager_host_container.DistributedVirtualSwitchManagerHostContainer
    
    .. py:attribute:: container
    
        Check compatibility of hosts in this container. The supported container types are Datacenter, Folder, and ComputeResource.
        
    
    .. py:attribute:: recursive
    
        If true, include hosts of all levels in the hierarchy with container as root of the tree. In case of container being a Datacenter, the recursive flag is applied to its HostFolder.
        
    