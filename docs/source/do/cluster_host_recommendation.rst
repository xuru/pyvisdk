
================================================================================
ClusterHostRecommendation
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_system.HostSystem`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.recommend_hosts_for_vm.RecommendHostsForVm`
    
.. class:: pyvisdk.do.cluster_host_recommendation.ClusterHostRecommendation
    
    .. py:attribute:: host
    
        The recommended host.
        
    
    .. py:attribute:: rating
    
        Rating for the recommendation. Ratings range from 1 to 5, and the higher the rating, the stronger DRS suggests this host is picked for the operation.
        
    