
==================================================================================================
VirtualSCSISharing
==================================================================================================

.. describe:: VirtualSCSISharing

    Sharing describes three possible ways of sharing the SCSI bus: One of these values is assigned to the sharedBus object to determine if or how the SCSI bus is shared.
    
    
    .. py:data:: VirtualSCSISharing.noSharing
    
        The virtual SCSI bus is not shared.
        
    
    .. py:data:: VirtualSCSISharing.physicalSharing
    
        The virtual SCSI bus is shared between two or more virtual machines residing on different physical hosts.
        
    
    .. py:data:: VirtualSCSISharing.virtualSharing
    
        The virtual SCSI bus is shared between two or more virtual machines. In this case, no physical machine is involved.
        
    