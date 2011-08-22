
================================================================================
DVSFailureCriteria
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.vmware_uplink_port_teaming_policy.VmwareUplinkPortTeamingPolicy`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.bool_policy.BoolPolicy`,
    :py:class:`~pyvisdk.do.int_policy.IntPolicy`,
    :py:class:`~pyvisdk.do.string_policy.StringPolicy`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.inheritable_policy.InheritablePolicy`
    
.. class:: pyvisdk.do.dvs_failure_criteria.DVSFailureCriteria
    
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
        
    