
================================================================================
PhysicalNic
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_network_info.HostNetworkInfo`,
    :py:class:`~pyvisdk.do.host_proxy_switch.HostProxySwitch`,
    :py:class:`~pyvisdk.do.host_virtual_switch.HostVirtualSwitch`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.physical_nic_link_info.PhysicalNicLinkInfo`,
    :py:class:`~pyvisdk.do.physical_nic_spec.PhysicalNicSpec`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.physical_nic.PhysicalNic
    
    .. py:attribute:: autoNegotiateSupported
    
        If set the flag indicates if the physical network adapter supports autonegotiate.
        
    
    .. py:attribute:: device
    
        The device name of the physical network adapter.
        
    
    .. py:attribute:: driver
    
        The name of the driver.
        
    
    .. py:attribute:: key
    
        The linkable identifier.
        
    
    .. py:attribute:: linkSpeed
    
        The current link state of the physical network adapter. If this object is not set, then the link is down.
        
    
    .. py:attribute:: mac
    
        The media access control (MAC) address of the physical network adapter.
        
    
    .. py:attribute:: pci
    
        Device hash of the PCI device corresponding to this physical network adapter.
        
    
    .. py:attribute:: resourcePoolSchedulerAllowed
    
        Flag indicating whether the NIC allows resource pool based scheduling for network I/O control.
        
    
    .. py:attribute:: resourcePoolSchedulerDisallowedReason
    
        If resourcePoolSchedulerAllowed is false, this property advertises the reason for disallowing resource scheduling on this NIC. The reasons may be one of PhysicalNicResourcePoolSchedulerDisallowedReason
        
    
    .. py:attribute:: spec
    
        The specification of the physical network adapter.
        
    
    .. py:attribute:: validLinkSpecification
    
        The valid combinations of speed and duplexity for this physical network adapter. The speed and the duplex settings usually must be configured as a pair. This array lists all the valid combinations available for a physical network adapter.
        
    
    .. py:attribute:: vmDirectPathGen2Supported
    
        Flag indicating whether the NIC supports VMDirectPath Gen 2. Note that this is only an indicator of the capabilities of this NIC, not of the whole host.
        
    
    .. py:attribute:: vmDirectPathGen2SupportedMode
    
        If vmDirectPathGen2Supported is true, this property advertises the VMDirectPath Gen 2 mode supported by this NIC (chosen from PhysicalNicVmDirectPathGen2SupportedMode). A mode may require that the associated vNetwork Distributed Switch have a particular ProductSpec in order for network passthrough to be possible.
        
    
    .. py:attribute:: wakeOnLanSupported
    
        Flag indicating whether the NIC is wake-on-LAN capable
        
    