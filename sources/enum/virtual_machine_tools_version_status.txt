
==================================================================================================
VirtualMachineToolsVersionStatus
==================================================================================================

.. describe:: VirtualMachineToolsVersionStatus

    Current version status of VMware Tools installed in the guest operating system.
    
    
    .. py:data:: VirtualMachineToolsVersionStatus.guestToolsCurrent
    
        VMware Tools is installed, and the version is current.
        
    
    .. py:data:: VirtualMachineToolsVersionStatus.guestToolsNeedUpgrade
    
        VMware Tools is installed, but the version is not current.
        
    
    .. py:data:: VirtualMachineToolsVersionStatus.guestToolsNotInstalled
    
        VMware Tools has never been installed.
        
    
    .. py:data:: VirtualMachineToolsVersionStatus.guestToolsUnmanaged
    
        VMware Tools is installed, but it is not managed by VMWare.
        
    