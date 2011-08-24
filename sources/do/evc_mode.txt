
================================================================================
EVCMode
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.capability.Capability`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_cpu_id_info.HostCpuIdInfo`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.element_description.ElementDescription`
    
.. class:: pyvisdk.do.evc_mode.EVCMode
    
    .. py:attribute:: guaranteedCPUFeatures
    
        Describes the CPU feature baseline associated with the EVC mode. On the cluster where a particular EVC mode is configured, those CPU features are guaranteed, either because the host hardware naturally matches those features or because CPU feature override is used to mask out differences and enforce a match.
        
    
    .. py:attribute:: track
    
        Identifiers for feature groups that are at least partially present in the guaranteedCPUFeatures array for this mode. Use this property to compare track values from two modes. Do not use this property to determine the presence or absence of specific features.
        
    
    .. py:attribute:: vendor
    
        CPU hardware vendor required for this mode.
        
    
    .. py:attribute:: vendorTier
    
        Index for ordering the set of modes that apply to a given CPU vendor. Use this property to compare vendor tier values from two modes. Do not use this property to determine the presence or absence of specific features.
        
    