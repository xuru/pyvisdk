
================================================================================
LicenseAssignmentManagerLicenseAssignment
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.license_manager_license_info.LicenseManagerLicenseInfo`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_assigned_licenses.QueryAssignedLicenses`
    
.. class:: pyvisdk.do.license_assignment_manager_license_assignment.LicenseAssignmentManagerLicenseAssignment
    
    .. py:attribute:: assignedLicense
    
        License assigned to the entity
        
    
    .. py:attribute:: entityDisplayName
    
        Display name of the entity
        
    
    .. py:attribute:: entityId
    
        Id for the entity
        
    
    .. py:attribute:: properties
    
        Additional properties associated with this assignment Some of the properties are: "inUseFeatures" -- Features in the license key that are being used by the entity "ProductName" -- Name of the entity. Should match the product name of the assigned license. "ProductVersion" -- Version of the entity. Should match the product version of the assigned license. "Evaluation" -- EvaluationInfo object representing the evaluation left for the entity.
        
    
    .. py:attribute:: scope
    
        Scope of the entityId
        
    