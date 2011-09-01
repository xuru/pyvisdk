
==================================================================================================
VirtualMachineConnectionState
==================================================================================================

.. describe:: VirtualMachineConnectionState

    The connectivity state of a virtual machine. When the API is provided directly by a server product, such as ESX Server, then the disconnected state is not possible. However, when accessed through VirtualCenter, the state of a virtual machine is set to disconnected if the hosts that manage the virtual machine becomes unavailable.
    
    
    .. py:data:: VirtualMachineConnectionState.connected
    
        The server has access to the virtual machine.
        
    
    .. py:data:: VirtualMachineConnectionState.disconnected
    
        The server is currently disconnected from the virtual machine, since its host is disconnected. See general comment for this enumerated type for more details.
        
    
    .. py:data:: VirtualMachineConnectionState.inaccessible
    
        One or more of the virtual machine configuration files are inaccessible. For example, this can be due to transient disk failures. In this case, no configuration can be returned for a virtual machine.
        
    
    .. py:data:: VirtualMachineConnectionState.invalid
    
        The virtual machine configuration format is invalid. Thus, it is accessible on disk, but corrupted in a way that does not allow the server to read the content. In this case, no configuration can be returned for a virtual machine.
        
    
    .. py:data:: VirtualMachineConnectionState.orphaned
    
        The virtual machine is no longer registered on the host it is associated with. For example, a virtual machine that is unregistered or deleted directly on a host managed by VirtualCenter shows up in this state.
        
    