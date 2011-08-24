
================================================================================
VirtualHardwareOption
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_machine_config_option.VirtualMachineConfigOption`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.int_option.IntOption`,
    :py:class:`~pyvisdk.do.long_option.LongOption`,
    :py:class:`~pyvisdk.do.resource_config_option.ResourceConfigOption`,
    :py:class:`~pyvisdk.do.virtual_device_option.VirtualDeviceOption`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.virtual_hardware_option.VirtualHardwareOption
    
    .. py:attribute:: deviceListReadonly
    
        Whether the set of virtual devices can be changed, e.g., can devices be added or removed. This does not preclude changing devices.
        
    
    .. py:attribute:: hwVersion
    
        The virtual hardware version.
        
    
    .. py:attribute:: licensingLimit
    
        List of propery names which limits are given be a licensing restriction of the underlying product, e.g., a limit that is not derived based on the product or hardware features. For example, the property name "numCPU"
        
    
    .. py:attribute:: memoryMB
    
        The minimum, maximum, and default memory options, in MB, per virtual machine, for this VirtualHardwareOption. These values are typically overruled by the supported and recommended values specified in the GuestOsDescriptor class.
        
    
    .. py:attribute:: numCPU
    
        List of acceptable values for the number of CPUs supported by this ConfigOption. This is usually superceded by the information available in the guest operating system descriptors. The guest operating system descriptor describes a maximum CPU count, but the acceptable values are still constrained to the set specified here. The default value is stored at index 0 in the list.
        
    
    .. py:attribute:: numCpuReadonly
    
        Can the number of virtual CPUs be changed
        
    
    .. py:attribute:: numIDEControllers
    
        The minimum, maximum, and default number of IDE controllers for this virtual machine configuration. Note: SCSI controllers sit on the PCI controller so their options (minimum, maximum, and default values) are contained inside the VirtualPCIControllerOption class.
        
    
    .. py:attribute:: numPCIControllers
    
        The minimum, maximum, and default number of PCI controllers for this virtual machine configuration.
        
    
    .. py:attribute:: numPS2Controllers
    
        The minimum, maximum, and default number of PS2 controllers for this virtual machine configuration.
        
    
    .. py:attribute:: numSIOControllers
    
        The minimum, maximum, and default number of SIO controllers for this virtual machine configuration.
        
    
    .. py:attribute:: numSupportedWwnNodes
    
        The minimum, maximum and default number of NPIV WorldWidePort names supported for this virtual machine configuration.
        
    
    .. py:attribute:: numSupportedWwnPorts
    
        The minimum, maximum and default number of NPIV WorldWideNode names supported for this virtual machine configuration.
        
    
    .. py:attribute:: numUSBControllers
    
        The minimum, maximum, and default number of USB controllers for this virtual machine configuration.
        
    
    .. py:attribute:: resourceConfigOption
    
        Default value and value range for ResourceConfigOption
        
    
    .. py:attribute:: virtualDeviceOption
    
        Array of virtual device options valid for this virtual machine configuration. The list is unordered.
        
    