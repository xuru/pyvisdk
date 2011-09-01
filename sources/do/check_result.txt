
================================================================================
CheckResult
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_system.HostSystem`,
    :py:class:`~pyvisdk.do.localized_method_fault.LocalizedMethodFault`,
    :py:class:`~pyvisdk.do.virtual_machine.VirtualMachine`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.check_compatibility__task.CheckCompatibility_Task`,
    :py:meth:`~pyvisdk.do.check_migrate__task.CheckMigrate_Task`,
    :py:meth:`~pyvisdk.do.check_relocate__task.CheckRelocate_Task`,
    :py:meth:`~pyvisdk.do.query_v_motion_compatibility_ex__task.QueryVMotionCompatibilityEx_Task`
    
.. class:: pyvisdk.do.check_result.CheckResult
    
    .. py:attribute:: error
    
        A list of faults representing problems which are fatal to the operation. For VirtualMachineProvisioningChecker an error means that the given provisioning operation would fail. For VirtualMachineCompatibilityChecker an error means that either a power-on of this virtual machine would fail, or that the virtual machine would not run correctly once powered-on.
        
    
    .. py:attribute:: host
    
        The host involved in the testing.
        
    
    .. py:attribute:: vm
    
        The virtual machine involved in the testing.
        
    
    .. py:attribute:: warning
    
        A list of faults representing problems which may require attention, but which are not fatal.
        
    