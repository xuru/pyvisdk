
================================================================================
ToolsConfigInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_machine_config_info.VirtualMachineConfigInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_config_spec.VirtualMachineConfigSpec`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.tools_config_info.ToolsConfigInfo
    
    .. py:attribute:: afterPowerOn
    
        Flag to specify whether or not scripts should run after the virtual machine powers on.
        
    
    .. py:attribute:: afterResume
    
        Flag to specify whether or not scripts should run after the virtual machine resumes.
        
    
    .. py:attribute:: beforeGuestReboot
    
        Flag to specify whether or not scripts should run before the virtual machine reboots.
        
    
    .. py:attribute:: beforeGuestShutdown
    
        Flag to specify whether or not scripts should run before the virtual machine powers off.
        
    
    .. py:attribute:: beforeGuestStandby
    
        Flag to specify whether or not scripts should run before the virtual machine suspends.
        
    
    .. py:attribute:: pendingCustomization
    
        When set, this indicates that a customization operation is pending on the VM. The value represents the filename of the customization package on the host.
        
    
    .. py:attribute:: syncTimeWithHost
    
        Indicates whether or not the tools program will sync time with the host time.
        
    
    .. py:attribute:: toolsUpgradePolicy
    
        Tools upgrade policy setting for the virtual machine.See UpgradePolicy
        
    
    .. py:attribute:: toolsVersion
    
        Version of VMware Tools installed on the guest operating system.
        
    