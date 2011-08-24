
================================================================================
ClusterProfileConfigServiceCreateSpec
================================================================================


.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.cluster_profile_config_spec.ClusterProfileConfigSpec`
    
.. class:: pyvisdk.do.cluster_profile_config_service_create_spec.ClusterProfileConfigServiceCreateSpec
    
    .. py:attribute:: serviceType
    
        Type of the service for which the ClusterProfile is being requested. If more than one service is specified, the created ClusterProfile will cater for all the services. Possible values are specified by ClusterProfileServiceType. If unset, clear the compliance expressions on the profile.
        
    