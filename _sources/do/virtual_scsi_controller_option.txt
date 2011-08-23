
================================================================================
VirtualSCSIControllerOption
================================================================================


.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.para_virtual_scsi_controller_option.ParaVirtualSCSIControllerOption`,
    :py:class:`~pyvisdk.do.virtual_bus_logic_controller_option.VirtualBusLogicControllerOption`,
    :py:class:`~pyvisdk.do.virtual_lsi_logic_controller_option.VirtualLsiLogicControllerOption`,
    :py:class:`~pyvisdk.do.virtual_lsi_logic_sas_controller_option.VirtualLsiLogicSASControllerOption`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.bool_option.BoolOption`,
    :py:class:`~pyvisdk.do.int_option.IntOption`,
    :py:class:`~pyvisdk.do.virtual_scsi_sharing.VirtualSCSISharing`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.virtual_controller_option.VirtualControllerOption`
    
.. class:: pyvisdk.do.virtual_scsi_controller_option.VirtualSCSIControllerOption
    
    .. py:attribute:: defaultSharedIndex
    
        Index into sharing array specifying the default value.
        
    
    .. py:attribute:: hotAddRemove
    
        This object determines if hot adding and removing of devices is supported. Hot adding and removing of devices enables users to add or remove a SCSI disk without having to shut down the virtual machine. If the feature is supported, you can designate a default value. Two properties accomplish this: *
        
    
    .. py:attribute:: numSCSICdroms
    
        Three properties (numSCSICdroms.min, numSCSICdroms.max, and numSCSICdroms.defaultValue) define the minimum, maximum, and default number of SCSI VirtualCdrom instances available in the SCSI controller. The number of SCSI VirtualCdrom instances is also limited by the number of available slots in the SCSI controller.
        
    
    .. py:attribute:: numSCSIDisks
    
        Three properties (numSCSIDisks.min, numSCSIDisks.max, and numSCSIDisks.defaultValue) define the minimum, maximum, and default number of SCSI VirtualDisk instances available at any given time in the SCSI controller. The number of SCSI VirtualDisk instances is also limited by the number of available slots in the SCSI controller.
        
    
    .. py:attribute:: numSCSIPassthrough
    
        Three properties (numSCSIPassthrough.min, numSCSIPassthrough.max, and numSCSIPassthrough.defaultValue) define the minimum, maximum, and default number of VirtualSCSIPassthrough instances available have at any given time in the SCSI controller. The number of VirtualSCSIPassthrough instances is also limited by the number of available slots in the SCSI controller.
        
    
    .. py:attribute:: scsiCtlrUnitNumber
    
        The unit number of the SCSI controller. The SCSI controller sits on its own bus, so that this field defines which slot the controller will use.
        
    
    .. py:attribute:: sharing
    
        Supported shared bus modes.
        
    