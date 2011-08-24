
================================================================================
ProfileExpression
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.compliance_profile.ComplianceProfile`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.profile_composite_expression.ProfileCompositeExpression`,
    :py:class:`~pyvisdk.do.profile_simple_expression.ProfileSimpleExpression`
    
.. class:: pyvisdk.do.profile_expression.ProfileExpression
    
    .. py:attribute:: displayName
    
        User visible display name
        
    
    .. py:attribute:: id
    
        Identifier of this expression. The id has to be unique within a Profile. The id can be used as a key while building composite expressions.
        
    
    .. py:attribute:: negated
    
        Flag indicating if the condition of the expression should be negated. e.g: conditions like VSwitch0 has vmnic0 connected to it can be turned into VSwitch0 doesn't have vmnic0 connected to it.
        
    