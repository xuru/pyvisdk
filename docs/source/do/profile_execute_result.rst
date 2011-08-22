
================================================================================
ProfileExecuteResult
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_config_spec.HostConfigSpec`,
    :py:class:`~pyvisdk.do.profile_deferred_policy_option_parameter.ProfileDeferredPolicyOptionParameter`,
    :py:class:`~pyvisdk.do.profile_execute_error.ProfileExecuteError`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.execute_host_profile.ExecuteHostProfile`
    
.. class:: pyvisdk.do.profile_execute_result.ProfileExecuteResult
    
    .. py:attribute:: configSpec
    
        configSpec will be valid only if status == success
        
    
    .. py:attribute:: error
    
        List of errors that were encountered during execute. This field will be set if status is set to error.
        
    
    .. py:attribute:: inapplicablePath
    
        List of paths that are not applicable for this execute. e.g: If the precheck policies do not pass on a PortGroup, PortGroup will not be created. The user can ignore this subtree. This might be used the UI to not show the particular part of the tree.
        
    
    .. py:attribute:: requireInput
    
        List of paths that still need user Input. This can be used by the UI to highlight the particular fields. In future this could be used to ask the user for input in multiple rounds instead of filling up the whole input at once. Here is an illustration: In the first pass, the user just fills up bare minimum inputs needed. Once that data is sent to the server, the server evaluates the Profile and might decide to invalidate a particular part of the subtree or enable a new subtree in the profile. Which would result in a new set of invalidPaths and requireInput propertyPaths. The caller (UI) can keep calling the function in multiple steps till success. If there are values that are filled in in the previous iteration, they will be returned in requireInput[].param.
        
    
    .. py:attribute:: status
    
        Status of the execute operation Will be one of the enumerations in #Status
        
    