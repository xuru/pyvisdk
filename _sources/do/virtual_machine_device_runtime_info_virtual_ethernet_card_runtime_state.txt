
================================================================================
VirtualMachineDeviceRuntimeInfoVirtualEthernetCardRuntimeState
================================================================================


.. describe:: Since
    
    vSphere API 4.1
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_machine_device_runtime_info_device_runtime_state.VirtualMachineDeviceRuntimeInfoDeviceRuntimeState`
    
.. class:: pyvisdk.do.virtual_machine_device_runtime_info_virtual_ethernet_card_runtime_state.VirtualMachineDeviceRuntimeInfoVirtualEthernetCardRuntimeState
    
    .. py:attribute:: vmDirectPathGen2Active
    
        Flag to indicate whether VMDirectPath Gen 2 is active on this device. If false, the reason(s) for inactivity will be provided in one or more of vmDirectPathGen2InactiveReasonVm, vmDirectPathGen2InactiveReasonOther, and vmDirectPathGen2InactiveReasonExtended.
        
    
    .. py:attribute:: vmDirectPathGen2InactiveReasonExtended
    
        If vmDirectPathGen2Active is false, this property may contain an explanation provided by the platform, beyond the reasons (if any) enumerated in vmDirectPathGen2InactiveReasonVm and/or vmDirectPathGen2InactiveReasonOther.
        
    
    .. py:attribute:: vmDirectPathGen2InactiveReasonOther
    
        If vmDirectPathGen2Active is false, this array will be populated with reasons for the inactivity that are not related to virtual machine state or configuration (chosen from VmDirectPathGen2InactiveReasonOther). Virtual machine related reasons for inactivity will be provided in vmDirectPathGen2InactiveReasonVm. If there is a reason for inactivity that cannot be described by the available constants, vmDirectPathGen2InactiveReasonExtended will be populated with an additional explanation provided by the platform.
        
    
    .. py:attribute:: vmDirectPathGen2InactiveReasonVm
    
        If vmDirectPathGen2Active is false, this array will be populated with reasons for the inactivity that are related to virtual machine state or configuration (chosen from VmDirectPathGen2InactiveReasonVm). Other reasons for inactivity will be provided in vmDirectPathGen2InactiveReasonOther. If there is a reason for inactivity that cannot be described by the available constants, vmDirectPathGen2InactiveReasonExtended will be populated with an additional explanation provided by the platform.
        
    