
================================================================================
FaultToleranceSecondaryOpResult
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.cluster_power_on_vm_result.ClusterPowerOnVmResult`,
    :py:class:`~pyvisdk.do.virtual_machine.VirtualMachine`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.create_secondary_vm__task.CreateSecondaryVM_Task`,
    :py:meth:`~pyvisdk.do.enable_secondary_vm__task.EnableSecondaryVM_Task`
    
.. class:: pyvisdk.do.fault_tolerance_secondary_op_result.FaultToleranceSecondaryOpResult
    
    .. py:attribute:: powerOnAttempted
    
        Whether an attempt was made to power on the secondary. If an attempt was made, powerOnResult will report the status of this attempt.
        
    
    .. py:attribute:: powerOnResult
    
        The powerOnResult property reports the outcome of powering on the Secondary VirtualMachine if a power on was required. A power on will be attempted if the Primary Virtual Machine is powered on when the operation is performed. This object is only reported if powerOnAttempted is true. If the outcome of the power-on attempt is not successful, the returned ClusterPowerOnVmResult object will include an instance of ClusterNotAttemptedVmInfo whereas if the attempt was successful, then an instance of ClusterAttemptedVmInfo is returned. When ClusterAttemptedVmInfo is returned, its task property is only set if the cluster is a HA-only cluster.
        
    
    .. py:attribute:: vm
    
        The Secondary VirtualMachine
        
    