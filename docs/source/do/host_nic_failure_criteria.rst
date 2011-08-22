
================================================================================
HostNicFailureCriteria
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_nic_teaming_policy.HostNicTeamingPolicy`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_nic_failure_criteria.HostNicFailureCriteria
    
    .. py:attribute:: checkBeacon
    
        The flag to indicate whether or not to enable this property to enable beacon probing as a method to validate the link status of a physical network adapter.
        
    
    .. py:attribute:: checkDuplex
    
        The flag to indicate whether or not to use the link duplex reported by the driver as link selection criteria.
        
    
    .. py:attribute:: checkErrorPercent
    
        The flag to indicate whether or not to use link error percentage to detect failure.
        
    
    .. py:attribute:: checkSpeed
    
        To use link speed as the criteria,
        
    
    .. py:attribute:: fullDuplex
    
        See checkDuplex
        
    
    .. py:attribute:: percentage
    
        See checkErrorPercent
        
    
    .. py:attribute:: speed
    
        See checkSpeed
        
    