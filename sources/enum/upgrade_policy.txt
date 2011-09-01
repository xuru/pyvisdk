
==================================================================================================
UpgradePolicy
==================================================================================================

.. describe:: UpgradePolicy

    The policy setting used to determine when tools are auto-upgraded for a virtual machine
    
    
    .. py:data:: UpgradePolicy.manual
    
        No auto-upgrades for tools will be performed for this virtual machine. Users must manually invoke the UpgradeTools operation to update the tools.
        
    
    .. py:data:: UpgradePolicy.upgradeAtPowerCycle
    
        When the virtual machine is power-cycled, the system checks for a newer version of tools when the VM comes back up. If it is available, a tools upgrade is automatically performed on the virtual machine and it is rebooted if necessary.
        
    