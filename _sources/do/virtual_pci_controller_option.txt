
================================================================================
VirtualPCIControllerOption
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.int_option.IntOption`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_controller_option.VirtualControllerOption`
    
.. class:: pyvisdk.do.virtual_pci_controller_option.VirtualPCIControllerOption
    
    .. py:attribute:: numEthernetCards
    
        Defines the minimum, maximum, and default number of VirtualEthernetCard instances available, at any given time, in the PCI controller. The number of VirtualEthernetCard instances is also limited by the number of available slots in the PCI controller.
        
    
    .. py:attribute:: numParaVirtualSCSIControllers
    
        Defines the minimum, maximum, and default number of ParaVirtualScsiController instances available, at any given time, in the PCI controller. This is also limited by the number of available PCI Express slots in the PCI controller as well as the total number of supported SCSI controllers.
        
    
    .. py:attribute:: numPCIPassthroughDevices
    
        Defines the minimum, maximum, and default number of VirtualPCIPassthrough instances available, at any given time, in the PCI controller. This is also limited by the number of available PCI Express slots in the PCI controller.
        
    
    .. py:attribute:: numSasSCSIControllers
    
        Defines the minimum, maximum, and default number of VirtualLsiLogicSASController instances available, at any given time, in the PCI controller. This is also limited by the number of available PCI Express slots in the PCI controller as well as the total number of supported SCSI controllers.
        
    
    .. py:attribute:: numSCSIControllers
    
        Defines the minimum, maximum, and default number of VirtualSCSIController instances available at any given time in the PCI controller. The number of VirtualSCSIController instances is also limited by the number of available slots in the PCI controller.
        
    
    .. py:attribute:: numSoundCards
    
        Defines the minimum, maximum, and default number of VirtualSoundCard instances available, at any given time, in the PCI controller. The number of VirtualSoundCard instances is also limited by the number of available slots in the PCI controller.
        
    
    .. py:attribute:: numVideoCards
    
        Defines the minimum, maximum, and default number of VirtualVideoCard instances available, at any given time, in the PCI controller. The number of VirtualVideoCard instances is also limited by the number of available slots in the PCI controller.
        
    
    .. py:attribute:: numVmciDevices
    
        Defines the minimum, maximum, and default number of VirtualVMCIDevice instances available, at any given time, in the PCI controller. This is also limited by the number of available slots in the PCI controller.
        
    
    .. py:attribute:: numVmiRoms
    
        Defines the minimum, maximum, and default number of VirtualVMIROM instances available, at any given time, in the PCI controller. This is also limited by the number of available slots in the PCI controller.
        
    
    .. py:attribute:: numVmxnet3EthernetCards
    
        Defines the minimum, maximum, and default number of VirtualVmxnet3 ethernet card instances available, at any given time, in the PCI controller. This is also limited by the number of available PCI Express slots in the PCI controller as well as the total number of supported ethernet cards.
        
    