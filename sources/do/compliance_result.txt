
================================================================================
ComplianceResult
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.compliance_failure.ComplianceFailure`,
    :py:class:`~pyvisdk.do.managed_entity.ManagedEntity`,
    :py:class:`~pyvisdk.do.profile.Profile`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.check_compliance__task.CheckCompliance_Task`,
    :py:meth:`~pyvisdk.do.check_profile_compliance__task.CheckProfileCompliance_Task`,
    :py:meth:`~pyvisdk.do.query_compliance_status.QueryComplianceStatus`
    
.. class:: pyvisdk.do.compliance_result.ComplianceResult
    
    .. py:attribute:: checkTime
    
        Time at which compliance check was last run on the entity
        
    
    .. py:attribute:: complianceStatus
    
        Indicates the compliance status of the entity. See
        
    
    .. py:attribute:: entity
    
        Entity on which the compliance check was carried out. Entity can be a Cluster, Host and so on.
        
    
    .. py:attribute:: failure
    
        If complianceStatus is non-compliant, failure will contain additional information about the compliance errors.
        
    
    .. py:attribute:: profile
    
        Profile for which the ComplianceResult applies
        
    