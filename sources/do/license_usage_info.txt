
================================================================================
LicenseUsageInfo
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.license_feature_info.LicenseFeatureInfo`,
    :py:class:`~pyvisdk.do.license_reservation_info.LicenseReservationInfo`,
    :py:class:`~pyvisdk.do.license_source.LicenseSource`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_license_usage.QueryLicenseUsage`
    
.. class:: pyvisdk.do.license_usage_info.LicenseUsageInfo
    
    .. py:attribute:: featureInfo
    
        Includes all the features that are referenced in the reservation array.
        
    
    .. py:attribute:: reservationInfo
    
        A list of feature reservations.
        
    
    .. py:attribute:: source
    
        The source from which licensing data is acquired.See LicenseSource
        
    
    .. py:attribute:: sourceAvailable
    
        Returns whether or not the source is currently available.See sourceAvailable
        
    