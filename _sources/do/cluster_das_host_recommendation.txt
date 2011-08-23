
================================================================================
ClusterDasHostRecommendation
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_system.HostSystem`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.cluster_das_host_recommendation.ClusterDasHostRecommendation
    
    .. py:attribute:: drsRating
    
        Rating as computed by DRS for a DRS-enabled cluster. Rating range from 1 to 5, and the higher the rating, the stronger DRS suggests this host is picked for the operation.
        
    
    .. py:attribute:: host
    
        The recommended host.
        
    