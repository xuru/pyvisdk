
================================================================================
VirtualMachineConfigOption
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.datastore_option.DatastoreOption`,
    :py:class:`~pyvisdk.do.guest_os_descriptor.GuestOsDescriptor`,
    :py:class:`~pyvisdk.do.virtual_device.VirtualDevice`,
    :py:class:`~pyvisdk.do.virtual_hardware_option.VirtualHardwareOption`,
    :py:class:`~pyvisdk.do.virtual_machine_capability.VirtualMachineCapability`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_config_option.QueryConfigOption`
    
.. class:: pyvisdk.do.virtual_machine_config_option.VirtualMachineConfigOption
    
    .. py:attribute:: capabilities
    
        Capabilities supported by a virtual machine.
        
    
    .. py:attribute:: datastore
    
        The datastore options for this virtual machine.
        
    
    .. py:attribute:: defaultDevice
    
        The list of virtual devices that are created on a virtual machine by default. Clients should not create these devices.
        
    
    .. py:attribute:: description
    
        A description string for this configOption.
        
    
    .. py:attribute:: guestOSDefaultIndex
    
        Index into guestOsDescriptor array denoting the default guest operating system.
        
    
    .. py:attribute:: guestOSDescriptor
    
        List of supported guest operating systems. The choice of guest operating system may limit the set of valid devices. For example, you cannot select Vmxnet with all guest operating systems.
        
    
    .. py:attribute:: hardwareOptions
    
        Processor, memory, and virtual device options for a virtual machine.
        
    
    .. py:attribute:: supportedMonitorType
    
        The monitor types supported by a host. The acceptable monitor types are enumerated by VirtualMachineFlagInfoMonitorType.
        
    
    .. py:attribute:: supportedOvfEnvironmentTransport
    
        Specifies the supported property transports that are available for the OVF environment
        
    
    .. py:attribute:: supportedOvfInstallTransport
    
        Specifies the supported transports for the OVF installation phase.
        
    
    .. py:attribute:: version
    
        The version corresponding to this configOption.
        
    