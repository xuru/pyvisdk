
================================================================================
VirtualMachineConfigSummary
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_machine_summary.VirtualMachineSummary`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.fault_tolerance_config_info.FaultToleranceConfigInfo`,
    :py:class:`~pyvisdk.do.v_app_product_info.VAppProductInfo`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.virtual_machine_config_summary.VirtualMachineConfigSummary
    
    .. py:attribute:: annotation
    
        Description for the virtual machine.
        
    
    .. py:attribute:: cpuReservation
    
        Configured CPU reservation in MHz
        
    
    .. py:attribute:: ftInfo
    
        Fault Tolerance settings for this virtual machine. This property will be populated only for fault tolerance virtual machines and will be left unset for all other virtual machines. See FaultToleranceConfigInfo for a description.
        
    
    .. py:attribute:: guestFullName
    
        Guest operating system name configured on the virtual machine.
        
    
    .. py:attribute:: guestId
    
        Guest operating system identifier (short name).
        
    
    .. py:attribute:: installBootRequired
    
        Whether the VM requires a reboot to finish installation. False if no vApp meta-data is configured.
        
    
    .. py:attribute:: instanceUuid
    
        VC-specific identifier of the virtual machine
        
    
    .. py:attribute:: memoryReservation
    
        Configured Memory reservation in MB
        
    
    .. py:attribute:: memorySizeMB
    
        Memory size of the virtual machine, in megabytes.
        
    
    .. py:attribute:: name
    
        Name of the virtual machine.
        
    
    .. py:attribute:: numCpu
    
        Number of processors in the virtual machine.
        
    
    .. py:attribute:: numEthernetCards
    
        Number of virtual network adapters.
        
    
    .. py:attribute:: numVirtualDisks
    
        Number of virtual disks attached to the virtual machine.
        
    
    .. py:attribute:: product
    
        Product information. References to properties in the URLs are expanded.
        
    
    .. py:attribute:: template
    
        Flag to determine whether or not this virtual machine is a template.
        
    
    .. py:attribute:: uuid
    
        Virtual machine BIOS identification.
        
    
    .. py:attribute:: vmPathName
    
        Path name to the configuration file for the virtual machine
        
    