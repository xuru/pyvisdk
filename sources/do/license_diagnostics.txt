
================================================================================
LicenseDiagnostics
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.license_manager.LicenseManager`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.license_manager_state.LicenseManagerState`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.license_diagnostics.LicenseDiagnostics
    
    .. py:attribute:: lastStatusUpdate
    
        A timestamp of when opState was last updated.
        
    
    .. py:attribute:: licenseFeatureUnknowns
    
        Counter to track Total number of license features parsed from License source that are not recognized. This value starts at zero and wraps at 2^32-1 to zero. Discontinuity: sourceLastChanged.
        
    
    .. py:attribute:: licenseRequestFailures
    
        Counter to track Total number of licenses requests that were not fulfilled (denied, timeout, or other). This value starts at zero and wraps at 2^32-1 to zero. Discontinuity: sourceLastChanged.
        
    
    .. py:attribute:: licenseRequests
    
        Counter to track total number of licenses requested. This value starts at zero and wraps at 2^32-1 to zero. Discontinuity: sourceLastChanged.
        
    
    .. py:attribute:: opFailureMessage
    
        A human readable reason when optState reports Fault condition.
        
    
    .. py:attribute:: opState
    
        The general state of the license subsystem.
        
    
    .. py:attribute:: sourceLastChanged
    
        A timestamp of when sourceAvailable last changed state, expressed in UTC.
        
    
    .. py:attribute:: sourceLatency
    
        Exponentially decaying average of the transaction time for license acquisition and routine communications with LicenseSource. Units: milliseconds.
        
    
    .. py:attribute:: sourceLost
    
        Counter to track number of times connection to source was lost. This value starts at zero and wraps at 2^32-1 to zero. Discontinuity: sourceLastChanged.
        
    