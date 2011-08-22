
================================================================================
ProfileCompositeExpression
================================================================================


.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.profile_expression.ProfileExpression`
    
.. class:: pyvisdk.do.profile_composite_expression.ProfileCompositeExpression
    
    .. py:attribute:: expressionName
    
        List of expression names that will be used for this composition. The individual expressions will return a boolean. The return values of the individual expressions will be used to compute the final return value of the CompositeExpression. The expressions specified in the list can themselves be CompositeExpressions.
        
    
    .. py:attribute:: operator
    
        Logical operator to be applied between the expressions in the composite expression. e.g: or, and
        
    