
================================================================================
ClusterAction
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.cluster_action_history.ClusterActionHistory`,
    :py:class:`~pyvisdk.do.cluster_recommendation.ClusterRecommendation`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.cluster_host_power_action.ClusterHostPowerAction`,
    :py:class:`~pyvisdk.do.cluster_initial_placement_action.ClusterInitialPlacementAction`,
    :py:class:`~pyvisdk.do.cluster_migration_action.ClusterMigrationAction`
    
.. class:: pyvisdk.do.cluster_action.ClusterAction
    
    .. py:attribute:: target
    
        The target object on which this action will be applied. For instance, a migration action will have a virtual machine as its target object, while a host power action will have a host as its target action.
        
    
    .. py:attribute:: type
    
        Type of the action. This is encoded to differentiate between different types of actions aimed at achieving different goals.
        
    