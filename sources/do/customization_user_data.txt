
================================================================================
CustomizationUserData
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.customization_sysprep.CustomizationSysprep`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.customization_name.CustomizationName`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.customization_user_data.CustomizationUserData
    
    .. py:attribute:: computerName
    
        The computer name of the (Windows) virtual machine. Computer name may contain letters (A-Z), numbers(0-9) and hyphens (-) but no spaces or periods (.). The name may not consists entirely of digits. On Vista computer name is restricted to 15 characters in length. If the computer name is longer than 15 characters, it will be truncated to 15 characters.
        
    
    .. py:attribute:: fullName
    
        User's full name.
        
    
    .. py:attribute:: orgName
    
        User's organization.
        
    
    .. py:attribute:: productId
    
        Microsoft Sysprep requires that a valid serial number be included in the answer file when mini-setup runs. This serial number is ignored if the original guest operating system was installed using a volume-licensed CD.
        
    