
================================================================================
VirtualMachineRuntimeInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_machine.VirtualMachine`,
    :py:class:`~pyvisdk.do.virtual_machine_summary.VirtualMachineSummary`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_system.HostSystem`,
    :py:class:`~pyvisdk.do.virtual_machine_connection_state.VirtualMachineConnectionState`,
    :py:class:`~pyvisdk.do.virtual_machine_device_runtime_info.VirtualMachineDeviceRuntimeInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_fault_tolerance_state.VirtualMachineFaultToleranceState`,
    :py:class:`~pyvisdk.do.virtual_machine_power_state.VirtualMachinePowerState`,
    :py:class:`~pyvisdk.do.virtual_machine_question_info.VirtualMachineQuestionInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_record_replay_state.VirtualMachineRecordReplayState`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.virtual_machine_runtime_info.VirtualMachineRuntimeInfo
    
    .. py:attribute:: bootTime
    
        The timestamp when the virtual machine was most recently powered on.
        
    
    .. py:attribute:: cleanPowerOff
    
        For a powered off virtual machine, indicates whether the virtual machine's last shutdown was an orderly power off or not. Unset if the virtual machine is running or suspended.
        
    
    .. py:attribute:: connectionState
    
        Indicates whether or not the virtual machine is available for management.
        
    
    .. py:attribute:: device
    
        Per-device runtime info. This array will be empty if the host software does not provide runtime info for any of the device types currently in use by the virtual machine.
        
    
    .. py:attribute:: faultToleranceState
    
        The fault tolerance state of the virtual machine.
        
    
    .. py:attribute:: host
    
        The host that is responsible for running a virtual machine. This property is null if the virtual machine is not running and is not assigned to run on a particular host.
        
    
    .. py:attribute:: maxCpuUsage
    
        Current upper-bound on CPU usage. The upper-bound is based on the host the virtual machine is current running on, as well as limits configured on the virtual machine itself or any parent resource pool. Valid while the virtual machine is running.
        
    
    .. py:attribute:: maxMemoryUsage
    
        Current upper-bound on memory usage. The upper-bound is based on memory configuration of the virtual machine, as well as limits configured on the virtual machine itself or any parent resource pool. Valid while the virtual machine is running.
        
    
    .. py:attribute:: memoryOverhead
    
        The amount of memory resource (in bytes) that will be used by the virtual machine above its guest memory requirements. This value is set if and only if the virtual machine is registered on a host that supports memory resource allocation features.
        
    
    .. py:attribute:: minRequiredEVCModeKey
    
        For a powered-on or suspended virtual machine in a cluster with Enhanced VMotion Compatibility (EVC) enabled, this identifies the least-featured EVC mode (among those for the appropriate CPU vendor) that could admit the virtual machine. See EVCMode. This property will be unset if the virtual machine is powered off or is not in an EVC cluster.
        
    
    .. py:attribute:: needSecondaryReason
    
        If set, indicates the reason the virtual machine needs a secondary.
        
    
    .. py:attribute:: numMksConnections
    
        Number of active MKS connections to this virtual machine.
        
    
    .. py:attribute:: powerState
    
        The current power state of the virtual machine.
        
    
    .. py:attribute:: question
    
        The current question, if any, that is blocking the virtual machine's execution.
        
    
    .. py:attribute:: recordReplayState
    
        Record / replay state of this virtual machine.
        
    
    .. py:attribute:: suspendInterval
    
        The total time the virtual machine has been suspended since it was initially powered on. This time excludes the current period, if the virtual machine is currently suspended. This property is updated when the virtual machine resumes, and is reset to zero when the virtual machine is powered off.
        
    
    .. py:attribute:: suspendTime
    
        The timestamp when the virtual machine was most recently suspended.
        
    
    .. py:attribute:: toolsInstallerMounted
    
        Flag to indicate whether or not the VMware Tools installer is mounted as a CD-ROM.
        
    