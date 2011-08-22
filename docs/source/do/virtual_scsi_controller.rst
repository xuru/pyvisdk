
================================================================================
VirtualSCSIController
================================================================================


.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.para_virtual_scsi_controller.ParaVirtualSCSIController`,
    :py:class:`~pyvisdk.do.virtual_bus_logic_controller.VirtualBusLogicController`,
    :py:class:`~pyvisdk.do.virtual_lsi_logic_controller.VirtualLsiLogicController`,
    :py:class:`~pyvisdk.do.virtual_lsi_logic_sas_controller.VirtualLsiLogicSASController`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.virtual_scsi_sharing.VirtualSCSISharing`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_controller.VirtualController`
    
.. class:: pyvisdk.do.virtual_scsi_controller.VirtualSCSIController
    
    .. py:attribute:: hotAddRemove
    
        Setting this flag is optional. Setting this flag to true enables hot adding devices; setting this flag to false disables hot adding. This property determines if a SCSI disk may be added without shutting down the virtual machine. Using this flag depends on if this feature is supported, as designated by the setting of the boolean hotAddRemove.supported property in the VirtualSCSIControllerOption data object type. *
        
    
    .. py:attribute:: scsiCtlrUnitNumber
    
        The unit number of the SCSI controller. The SCSI controller sits on its own bus, so this field defines which slot the controller is using.
        
    
    .. py:attribute:: sharedBus
    
        Mode for sharing the SCSI bus. The modes are physicalSharing, virtualSharing, and noSharing. See the Sharing data object type for an explanation of these modes.
        
    