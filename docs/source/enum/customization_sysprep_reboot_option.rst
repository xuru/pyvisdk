
==================================================================================================
CustomizationSysprepRebootOption
==================================================================================================

.. describe:: CustomizationSysprepRebootOption

    A enum constant specifying what should be done to the guest vm after running sysprep.
    
    
    .. py:data:: CustomizationSysprepRebootOption.noreboot
    
        Take no action. Leave the guest os running after running sysprep. This option can be used to look at values for debugging purposes after running sysprep.
        
    
    .. py:data:: CustomizationSysprepRebootOption.reboot
    
        Reboot the machine after running sysprep. This will cause values specified in the sysprep.inf to be applied immediately.
        
    
    .. py:data:: CustomizationSysprepRebootOption.shutdown
    
        Shutdown the machine after running sysprep. This puts the vm in a sealed state.
        
    