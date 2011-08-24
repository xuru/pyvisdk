
================================================================================
VirtualMachineVMCIDevice
================================================================================


.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_device.VirtualDevice`
    
.. class:: pyvisdk.do.virtual_machine_vmci_device.VirtualMachineVMCIDevice
    
    .. py:attribute:: allowUnrestrictedCommunication
    
        Determines the extent of VMCI communication with this virtual machine. Set this property to true to allow VMCI communication with all virtual machines on the host and with trusted services. Set this property to false to allow VMCI communication only with trusted services such as the hypervisor on the host.
        
    
    .. py:attribute:: id
    
        Unique identifier for VMCI socket access to this virtual machine. Use this value to identify this virtual machine in calls to the VMCI Sockets API. Applications running on other virtual machines on this host will use this value to connect to this virtual machine. You can cast this value to a 32-bit unsigned integer.
        
    