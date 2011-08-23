
================================================================================
VirtualMachineImportSpec
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.resource_pool.ResourcePool`,
    :py:class:`~pyvisdk.do.virtual_machine_config_spec.VirtualMachineConfigSpec`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.import_spec.ImportSpec`
    
.. class:: pyvisdk.do.virtual_machine_import_spec.VirtualMachineImportSpec
    
    .. py:attribute:: configSpec
    
        Configuration for the virtual machine.
        
    
    .. py:attribute:: resPoolEntity
    
        If specified, this resource pool will be used as the parent resource pool and the virtual machine will be made a linked child to the parent vApp. This field is ignored for the root node in an ImportSpec tree.
        
    