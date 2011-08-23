
================================================================================
CompositePolicyOption
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.policy_option.PolicyOption`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.policy_option.PolicyOption`
    
.. class:: pyvisdk.do.composite_policy_option.CompositePolicyOption
    
    .. py:attribute:: option
    
        List of policy options that are composed and applicable for this composite policy option. The selected PolicyOptions in a CompositePolicyOption will be used in the policy. PolicyOptions need not be specified if they are not desired for the CompositePolicyOption. Order of PolicyOptions in the PolicyOption array is not significant. The host profile policy engine will not respect order of PolicyOptions. It will apply PolicyOptions in a pre-determined order. Clients of the API must produce PolicyOption in the same order as specified in the metadata.
        
    