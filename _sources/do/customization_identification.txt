
================================================================================
CustomizationIdentification
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.customization_sysprep.CustomizationSysprep`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.customization_password.CustomizationPassword`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.customization_identification.CustomizationIdentification
    
    .. py:attribute:: domainAdmin
    
        This is the domain user account used for authentication if the virtual machine is joining a domain. The user does not need to be a domain administrator, but the account must have the privileges required to add computers to the domain.
        
    
    .. py:attribute:: domainAdminPassword
    
        This is the password for the domain user account used for authentication if the virtual machine is joining a domain.
        
    
    .. py:attribute:: joinDomain
    
        The domain that the virtual machine should join. If this value is supplied, then domainAdmin and domainAdminPassword must also be supplied, and the workgroup name must be empty.
        
    
    .. py:attribute:: joinWorkgroup
    
        The workgroup that the virtual machine should join. If this value is supplied, then the domain name and authentication fields must be empty.
        
    