
================================================================================
VirtualMachineRelocateSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.check_relocate__task.CheckRelocate_Task`,
    :py:meth:`~pyvisdk.do.relocate_vm__task.RelocateVM_Task`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_machine_clone_spec.VirtualMachineCloneSpec`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.datastore.Datastore`,
    :py:class:`~pyvisdk.do.host_system.HostSystem`,
    :py:class:`~pyvisdk.do.resource_pool.ResourcePool`,
    :py:class:`~pyvisdk.do.virtual_machine_relocate_spec_disk_locator.VirtualMachineRelocateSpecDiskLocator`,
    :py:class:`~pyvisdk.do.virtual_machine_relocate_transformation.VirtualMachineRelocateTransformation`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.virtual_machine_relocate_spec.VirtualMachineRelocateSpec
    
    .. py:attribute:: datastore
    
        The datastore where the virtual machine should be located. If not specified, the current datastore is used.
        
    
    .. py:attribute:: disk
    
        An optional list that allows specifying the datastore location for each virtual disk.
        
    
    .. py:attribute:: diskMoveType
    
        Manner in which to move the virtual disk to the target datastore. The set of possible values is described in VirtualMachineRelocateDiskMoveOptions.
        
    
    .. py:attribute:: host
    
        The target host for the virtual machine. If not specified, * if resource pool is not specified, current host is used. * if resource pool is specified, and the target pool represents a stand-alone host, the host is used. * if resource pool is specified, and the target pool represents a DRS-enabled cluster, a host selected by DRS is used. * if resource pool is specified and the target pool represents a cluster without DRS enabled, an InvalidArgument exception be thrown.
        
    
    .. py:attribute:: pool
    
        The resource pool to which this virtual machine should be attached. For a relocate or clone operation to a virtual machine, if the argument is not supplied, the current resource pool of virtual machine is used. For a clone operation to a template, this argument is ignored. For a clone operation from a template to a virtual machine, this argument is required.
        
    
    .. py:attribute:: transform
    
        Transformation to perform on the disks. The backend is free to ignore this hint if it is not valid for the current operation. This can be used by clients, for example, to create sparse disks for templates.See VirtualMachineRelocateTransformation
        
    