
================================================================================
VirtualMachineBootOptions
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_machine_config_info.VirtualMachineConfigInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_config_spec.VirtualMachineConfigSpec`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.virtual_machine_boot_options.VirtualMachineBootOptions
    
    .. py:attribute:: bootDelay
    
        Delay in milliseconds before starting the boot sequence. The boot delay specifies a time interval between virtual machine power on or restart and the beginning of the boot sequence.
        
    
    .. py:attribute:: bootRetryDelay
    
        Delay in milliseconds before a boot retry. The boot retry delay specifies a time interval between virtual machine boot failure and the subsequent attempt to boot again. The virtual machine uses this value only if bootRetryEnabled is true.
        
    
    .. py:attribute:: bootRetryEnabled
    
        If set to
        
    
    .. py:attribute:: enterBIOSSetup
    
        If set to
        
    