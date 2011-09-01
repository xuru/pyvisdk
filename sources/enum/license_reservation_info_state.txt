
==================================================================================================
LicenseReservationInfoState
==================================================================================================

.. describe:: LicenseReservationInfoState

    Describes the reservation state of a license.
    
    
    .. py:data:: LicenseReservationInfoState.licensed
    
        The required number of licenses have been acquired from the license source.
        
    
    .. py:data:: LicenseReservationInfoState.noLicense
    
        This indicates that the license has expired or the system attempted to acquire the license but was not successful in reserving it.
        
    
    .. py:data:: LicenseReservationInfoState.notUsed
    
        This license is currently unused by the system, or the feature does not apply. For example, a DRS license appears as NotUsed if the host is not part of a DRS-enabled cluster.
        
    
    .. py:data:: LicenseReservationInfoState.unlicensedUse
    
        The LicenseManager failed to acquire a license but the implementation policy allows us to use the licensed feature anyway. This is possible, for example, when a license server becomes unavailable after a license had been successfully reserved from it.
        
    