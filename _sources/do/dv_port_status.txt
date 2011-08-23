
================================================================================
DVPortStatus
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.dv_port_state.DVPortState`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.numeric_range.NumericRange`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.dv_port_status.DVPortStatus
    
    .. py:attribute:: blocked
    
        Whether the port is blocked by switch implementation.
        
    
    .. py:attribute:: linkPeer
    
        The name of the connected entity.
        
    
    .. py:attribute:: linkUp
    
        Whether the port is in linkUp status.
        
    
    .. py:attribute:: macAddress
    
        The MAC address that is used at this port.
        
    
    .. py:attribute:: mtu
    
        The MTU of the port. Currently, this property can be set only at the switch level. Attempting to change it at the portgroup or port level raises an exception.
        
    
    .. py:attribute:: statusDetail
    
        Additional information regarding the port's current status.
        
    
    .. py:attribute:: trunkingMode
    
        True if the port VLAN tagging/stripping is disabled.
        
    
    .. py:attribute:: vlanIds
    
        The VLAN ID of the port.
        
    
    .. py:attribute:: vmDirectPathGen2Active
    
        Flag to indicate whether VMDirectPath Gen 2 is active on this port. If false, the reason(s) for inactivity will be provided in one or more of vmDirectPathGen2InactiveReasonNetwork, vmDirectPathGen2InactiveReasonOther, and vmDirectPathGen2InactiveReasonExtended.
        
    
    .. py:attribute:: vmDirectPathGen2InactiveReasonExtended
    
        If vmDirectPathGen2Active is false, this property may contain an explanation provided by the platform, beyond the reasons (if any) enumerated in vmDirectPathGen2InactiveReasonNetwork and/or vmDirectPathGen2InactiveReasonOther.
        
    
    .. py:attribute:: vmDirectPathGen2InactiveReasonNetwork
    
        If vmDirectPathGen2Active is false, this array will be populated with reasons for the inactivity that are related to network state or configuration (chosen from VmDirectPathGen2InactiveReasonNetwork). Other reasons for inactivity will be provided in vmDirectPathGen2InactiveReasonOther. If there is a reason for inactivity that cannot be described by the available constants, vmDirectPathGen2InactiveReasonExtended will be populated with an additional explanation provided by the platform.
        
    
    .. py:attribute:: vmDirectPathGen2InactiveReasonOther
    
        If vmDirectPathGen2Active is false, this array will be populated with reasons for the inactivity that are not related to network state or configuration (chosen from VmDirectPathGen2InactiveReasonOther). Network-related reasons for inactivity will be provided in vmDirectPathGen2InactiveReasonNetwork. If there is a reason for inactivity that cannot be described by the available constants, vmDirectPathGen2InactiveReasonExtended will be populated with an additional explanation provided by the platform.
        
    