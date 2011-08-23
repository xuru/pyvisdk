
================================================================================
CustomizationGuiUnattended
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.customization_sysprep.CustomizationSysprep`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.customization_password.CustomizationPassword`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.customization_gui_unattended.CustomizationGuiUnattended
    
    .. py:attribute:: autoLogon
    
        Flag to determine whether or not the machine automatically logs on as Administrator. See also the password property.
        
    
    .. py:attribute:: autoLogonCount
    
        If the AutoLogon flag is set, then the AutoLogonCount property specifies the number of times the machine should automatically log on as Administrator. Generally it should be 1, but if your setup requires a number of reboots, you may want to increase it. This number may be determined by the list of commands executed by the GuiRunOnce command.
        
    
    .. py:attribute:: password
    
        The new administrator password for the machine. To specify that the password should be set to blank (that is, no password), set the password value to NULL. Because of encryption, "" is NOT a valid value.
        
    
    .. py:attribute:: timeZone
    
        The time zone for the new virtual machine. Numbers correspond to time zones listed in sysprep documentation at in Microsoft Technet.
        
    