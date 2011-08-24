
================================================================================
HostCpuIdInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.evc_mode.EVCMode`,
    :py:class:`~pyvisdk.do.guest_os_descriptor.GuestOsDescriptor`,
    :py:class:`~pyvisdk.do.host_capability.HostCapability`,
    :py:class:`~pyvisdk.do.host_cpu_package.HostCpuPackage`,
    :py:class:`~pyvisdk.do.host_hardware_info.HostHardwareInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_config_info.VirtualMachineConfigInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_cpu_id_info_spec.VirtualMachineCpuIdInfoSpec`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_cpu_id_info.HostCpuIdInfo
    
    .. py:attribute:: eax
    
        String representing the required EAX bits.
        
    
    .. py:attribute:: ebx
    
        String representing the required EBX bits.
        
    
    .. py:attribute:: ecx
    
        String representing the required ECX bits.
        
    
    .. py:attribute:: edx
    
        String representing the required EDX bits.
        
    
    .. py:attribute:: level
    
        Level (EAX input to CPUID).
        
    
    .. py:attribute:: vendor
    
        Used if this mask is for a particular vendor.
        
    