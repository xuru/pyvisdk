
================================================================================
OvfValidateHostResult
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.localized_method_fault.LocalizedMethodFault`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.validate_host.ValidateHost`
    
.. class:: pyvisdk.do.ovf_validate_host_result.OvfValidateHostResult
    
    .. py:attribute:: downloadSize
    
        The total amount of data that must be transferred to download the entity.
        
    
    .. py:attribute:: error
    
        Errors that happened during validation. The presence of faults in this list indicates that the validation failed.
        
    
    .. py:attribute:: flatDeploymentSize
    
        The total amount of space required to deploy the entity if using flat disks.
        
    
    .. py:attribute:: sparseDeploymentSize
    
        The total amount of space required to deploy the entity using sparse disks, if known.
        
    
    .. py:attribute:: supportedDiskProvisioning
    
        An array of the disk provisioning type supported by the target host system.
        
    
    .. py:attribute:: warning
    
        Non-fatal warnings from the validation.
        
    