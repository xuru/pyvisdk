
==================================================================================================
VirtualMachineConfigSpecNpivWwnOp
==================================================================================================

.. describe:: VirtualMachineConfigSpecNpivWwnOp

    The root WWN operation mode.
    
    
    .. py:data:: VirtualMachineConfigSpecNpivWwnOp.extend
    
        Generate a new set of WWNs and append them to the existing list vSphere API 4.0
        
    
    .. py:data:: VirtualMachineConfigSpecNpivWwnOp.generate
    
        Generate a new set of WWNs and assign it to the virtual machine.
        
    
    .. py:data:: VirtualMachineConfigSpecNpivWwnOp.remove
    
        Remove the currently assigned WWNs from the virtual machine.
        
    
    .. py:data:: VirtualMachineConfigSpecNpivWwnOp.set
    
        Take a client-specified set of WWNs (specified in "wwn" property) and assign them to the virtual machine. If the new WWN quntity are more than existing then we will append them to the existing list of WWNs.
        
    