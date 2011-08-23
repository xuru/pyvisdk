
================================================================================
DistributedVirtualSwitchManagerCompatibilityResult
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_system.HostSystem`,
    :py:class:`~pyvisdk.do.localized_method_fault.LocalizedMethodFault`
    
.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_dvs_check_compatibility.QueryDvsCheckCompatibility`
    
.. class:: pyvisdk.do.distributed_virtual_switch_manager_compatibility_result.DistributedVirtualSwitchManagerCompatibilityResult
    
    .. py:attribute:: error
    
        This property contains the faults that makes the host not compatible with a given DvsProductSpec. For example, a host might not be compatible because it's an older version of ESX that doesn't support DVS.
        
    
    .. py:attribute:: host
    
        The host for which results are annotated. The whole object will be filtered out if the caller did not have view permissions on the host entity.
        
    