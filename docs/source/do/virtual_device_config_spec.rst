
================================================================================
VirtualDeviceConfigSpec
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_machine_config_spec.VirtualMachineConfigSpec`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.virtual_device.VirtualDevice`,
    :py:class:`~pyvisdk.do.virtual_device_config_spec_file_operation.VirtualDeviceConfigSpecFileOperation`,
    :py:class:`~pyvisdk.do.virtual_device_config_spec_operation.VirtualDeviceConfigSpecOperation`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.virtual_device_config_spec.VirtualDeviceConfigSpec
    
    .. py:attribute:: device
    
        Device specification, with all necessary properties set.
        
    
    .. py:attribute:: fileOperation
    
        Type of operation being performed on the backing of the specified virtual device. If no file operation is specified in the VirtualDeviceSpec, then any backing filenames in the VirtualDevice must refer to files that already exist. The "replace" and "delete" values for this property are only applicable to virtual disk backing files.
        
    
    .. py:attribute:: operation
    
        Type of operation being performed on the specified virtual device. If no operation is specified, the spec. is ignored.
        
    