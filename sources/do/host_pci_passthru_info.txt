
================================================================================
HostPciPassthruInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_config_info.HostConfigInfo`,
    :py:class:`~pyvisdk.do.host_pci_passthru_system.HostPciPassthruSystem`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_pci_passthru_info.HostPciPassthruInfo
    
    .. py:attribute:: dependentDevice
    
        Device which needs to be unclaimed by vmkernel (may be bridge)
        
    
    .. py:attribute:: id
    
        The name ID of this PCI, composed of "bus:slot.function".
        
    
    .. py:attribute:: passthruActive
    
        Whether passThru is active for this device (meaning enabled + rebooted)
        
    
    .. py:attribute:: passthruCapable
    
        Whether passThru is even possible for this device (decided by vmkctl)
        
    
    .. py:attribute:: passthruEnabled
    
        Whether passThru has been configured by the user
        
    