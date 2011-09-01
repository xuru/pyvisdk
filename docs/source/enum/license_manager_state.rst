
==================================================================================================
LicenseManagerState
==================================================================================================

.. describe:: LicenseManagerState

    State of licensing subsystem.
    
    
    .. py:data:: LicenseManagerState.fault
    
        Initialization has failed or grace period expired.
        
    
    .. py:data:: LicenseManagerState.initializing
    
        Setting or resetting configuration in progress.
        
    
    .. py:data:: LicenseManagerState.marginal
    
        License source unavailable, using license cache.
        
    
    .. py:data:: LicenseManagerState.normal
    
        Running within operating parameters.
        
    