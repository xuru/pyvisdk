
================================================================================
ClusterRecommendation
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.cluster_compute_resource.ClusterComputeResource`,
    :py:class:`~pyvisdk.do.cluster_power_on_vm_result.ClusterPowerOnVmResult`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.cluster_action.ClusterAction`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.cluster_recommendation.ClusterRecommendation
    
    .. py:attribute:: action
    
        List of actions that are executed as part of this recommendation
        
    
    .. py:attribute:: key
    
        Key to identify the recommendation when calling applyRecommendation.
        
    
    .. py:attribute:: prerequisite
    
        This recommendation may depend on some other recommendations. The prerequisite recommendations are listed by their keys.
        
    
    .. py:attribute:: rating
    
        A rating of the recommendation. Valid values range from 1 (lowest confidence) to 5 (highest confidence).
        
    
    .. py:attribute:: reason
    
        A reason code explaining why this set of migrations is being suggested.
        
    
    .. py:attribute:: reasonText
    
        Text that provides more information about the reason code for the suggested set of migrations.
        
    
    .. py:attribute:: target
    
        The target object of this recommendation.
        
    
    .. py:attribute:: time
    
        The time this recommendation was computed.
        
    
    .. py:attribute:: type
    
        Type of the recommendation. This differentiates between various of recommendations aimed at achieving different goals.
        
    