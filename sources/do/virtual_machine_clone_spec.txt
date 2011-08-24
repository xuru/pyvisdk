
================================================================================
VirtualMachineCloneSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.clone_vm__task.CloneVM_Task`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.customization_spec.CustomizationSpec`,
    :py:class:`~pyvisdk.do.virtual_machine_config_spec.VirtualMachineConfigSpec`,
    :py:class:`~pyvisdk.do.virtual_machine_relocate_spec.VirtualMachineRelocateSpec`,
    :py:class:`~pyvisdk.do.virtual_machine_snapshot.VirtualMachineSnapshot`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.virtual_machine_clone_spec.VirtualMachineCloneSpec
    
    .. py:attribute:: config
    
        An optional specification of changes to the virtual hardware. For example, this can be used to, (but not limited to) reconfigure the networks the virtual switches are hooked up to in the cloned virtual machine.
        
    
    .. py:attribute:: customization
    
        An optional guest operating system customization specification. This value is ignored if a template is being created.
        
    
    .. py:attribute:: location
    
        A type of RelocateSpec that specifies the location of resources the newly cloned virtual machine will use. The location specifies: * A datastore where the virtual machine will be located on physical storage. This is always provided because it indicates where the newly created close will be copied. * a resource pool and optionally a host. The resource pool determines what compute resources will be available to the clone and the host indicates which machine will host the clone.
        
    
    .. py:attribute:: powerOn
    
        Specifies whether or not the new VirtualMachine should be powered on after creation. As part of a customization, this flag is normally set to true, since the first power-on operation completes the customization process. This flag is ignored if a template is being created.
        
    
    .. py:attribute:: snapshot
    
        Snapshot reference from which to base the clone.
        
    
    .. py:attribute:: template
    
        Specifies whether or not the new virtual machine should be marked as a template.
        
    