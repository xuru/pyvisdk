
================================================================================
ProfilePolicyOptionMetadata
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.profile_policy_metadata.ProfilePolicyMetadata`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.extended_element_description.ExtendedElementDescription`,
    :py:class:`~pyvisdk.do.profile_parameter_metadata.ProfileParameterMetadata`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.profile_composite_policy_option_metadata.ProfileCompositePolicyOptionMetadata`,
    :py:class:`~pyvisdk.do.user_input_required_parameter_metadata.UserInputRequiredParameterMetadata`
    
.. class:: pyvisdk.do.profile_policy_option_metadata.ProfilePolicyOptionMetadata
    
    .. py:attribute:: id
    
        The id of the PolicyOption id.key Identifies the PolicyOption type. id.label contains a brief localizable message describing the PolicyOption. id.summary contains a localizable summary of the PolicyOption. Summary information can contain embedded variable names which can be replaced with values from #parameter.
        
    
    .. py:attribute:: parameter
    
        Metadata about the parameters of the PolicyOption. The parameter can be a derived class of PolicyOptionParameterMetadata too.
        
    