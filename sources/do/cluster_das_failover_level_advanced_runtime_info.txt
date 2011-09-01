
================================================================================
ClusterDasFailoverLevelAdvancedRuntimeInfo
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.cluster_das_failover_level_advanced_runtime_info_host_slots.ClusterDasFailoverLevelAdvancedRuntimeInfoHostSlots`,
    :py:class:`~pyvisdk.do.cluster_das_failover_level_advanced_runtime_info_slot_info.ClusterDasFailoverLevelAdvancedRuntimeInfoSlotInfo`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.cluster_das_advanced_runtime_info.ClusterDasAdvancedRuntimeInfo`
    
.. class:: pyvisdk.do.cluster_das_failover_level_advanced_runtime_info.ClusterDasFailoverLevelAdvancedRuntimeInfo
    
    .. py:attribute:: hostSlots
    
        
        
    
    .. py:attribute:: slotInfo
    
        Slot information for this cluster.
        
    
    .. py:attribute:: totalGoodHosts
    
        The total number of connected hosts that are not in maintance mode and that do not have any DAS-related config issues on them.
        
    
    .. py:attribute:: totalHosts
    
        The total number of hosts in the cluster.
        
    
    .. py:attribute:: totalSlots
    
        The total number of slots available in the cluster.See SlotInfo
        
    
    .. py:attribute:: totalVms
    
        The total number of powered on vms in the cluster.
        
    
    .. py:attribute:: unreservedSlots
    
        The number of slots that are not used by currently powered on virtual machines and not reserved to satisfy the configured failover level. This number gives an indication of how many additional virtual machines can be powered on in this cluster without violating the failover level (assuming the new virtual machine's reservations are satisfied by the current slot size). This value is computed as follows (where m is the configured failover level): Remove the m largest hosts (ie. the ones with the most slots) from the list of "good" hosts (see totalGoodHosts). Sum up the number of slots on the remaining hosts and deduct the number of currently used slots (see usedSlots). If this number is negative, use zero instead.See SlotInfo
        
    
    .. py:attribute:: usedSlots
    
        The number of slots currently being used.See SlotInfo
        
    