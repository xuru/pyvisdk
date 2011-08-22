
================================================================================
LicenseFeatureInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.license_availability_info.LicenseAvailabilityInfo`,
    :py:class:`~pyvisdk.do.license_expired_event.LicenseExpiredEvent`,
    :py:class:`~pyvisdk.do.license_manager.LicenseManager`,
    :py:class:`~pyvisdk.do.license_usage_info.LicenseUsageInfo`,
    :py:class:`~pyvisdk.do.no_license_event.NoLicenseEvent`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.license_feature_info_state.LicenseFeatureInfoState`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_supported_features.QuerySupportedFeatures`
    
.. class:: pyvisdk.do.license_feature_info.LicenseFeatureInfo
    
    .. py:attribute:: costUnit
    
        Each license has a cost associated with it and the value of costUnit specifies the applicable unit.
        
    
    .. py:attribute:: dependentKey
    
        Report List of feature keys used by this edition.
        
    
    .. py:attribute:: edition
    
        Flag to indicate whether the feature is an edition.
        
    
    .. py:attribute:: expiresOn
    
        Date representing the expiration date
        
    
    .. py:attribute:: featureDescription
    
        A human readable description of what function this feature enables.
        
    
    .. py:attribute:: featureName
    
        The display string for the feature name.
        
    
    .. py:attribute:: key
    
        Unique identifier for license as defined in License source data. Max length of this string is 64 characters of ASCII/ISO Latin-1 character set.
        
    
    .. py:attribute:: sourceRestriction
    
        Describe any restriction on the source of a license for this feature.
        
    
    .. py:attribute:: state
    
        Describes the state of the feature based on the current edition license. This property is unset for an edition license.
        
    