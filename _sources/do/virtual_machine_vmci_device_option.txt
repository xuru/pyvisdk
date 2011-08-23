
================================================================================
VirtualMachineVMCIDeviceOption
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.bool_option.BoolOption`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_device_option.VirtualDeviceOption`
    
.. class:: pyvisdk.do.virtual_machine_vmci_device_option.VirtualMachineVMCIDeviceOption
    
    .. py:attribute:: allowUnrestrictedCommunication
    
        Indicates support for VMCI communication and specifies the default operation. If defaultValue is set to true, the virtual machine can participate in VMCI communication with all other virtual machines on the host. Otherwise, VMCI communication will be restricted to trusted services such as the hypervisor on the host.
        
    