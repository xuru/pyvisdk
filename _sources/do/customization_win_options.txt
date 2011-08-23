
================================================================================
CustomizationWinOptions
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.customization_sysprep_reboot_option.CustomizationSysprepRebootOption`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.customization_options.CustomizationOptions`
    
.. class:: pyvisdk.do.customization_win_options.CustomizationWinOptions
    
    .. py:attribute:: changeSID
    
        The customization process should modify the machine's security identifier (SID). For Vista OS, SID will always be modified.
        
    
    .. py:attribute:: deleteAccounts
    
        If deleteAccounts is true, then all user accounts are removed from the system as part of the customization. Mini-setup creates a new Administrator account with a blank password.
        
    
    .. py:attribute:: reboot
    
        A value of type SysprepRebootOption specifying the action that should be taken after running sysprep. Defaults to "reboot".
        
    