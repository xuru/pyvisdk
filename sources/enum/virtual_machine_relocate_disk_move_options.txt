
==================================================================================================
VirtualMachineRelocateDiskMoveOptions
==================================================================================================

.. describe:: VirtualMachineRelocateDiskMoveOptions

    Specifies how a virtual disk is moved or copied to a datastore.In all cases after the move or copy the virtual machine's current running point will be placed on the target datastore. The current running point is defined as the disk backing which the virtual machine is currently writing to. This end state can be achieved in multiple ways, and the supported options are described in this enumeration.These options are only relevant when the backing of the specified disk is a file backing.Since disk backings may become shared as the result of either a clone operation or a relocate operation, PromoteDisks_Task has been provided as a way to unshare such disk backings.See parentSee parentSee parentSee parentSee parentSee diskMoveTypeSee diskMoveType
    
    
    .. py:data:: VirtualMachineRelocateDiskMoveOptions.createNewChildDiskBacking
    
        Create a new child disk backing on the destination datastore. None of the virtual disk's existing files should be moved from their current locations.
        
    
    .. py:data:: VirtualMachineRelocateDiskMoveOptions.moveAllDiskBackingsAndAllowSharing
    
        All of the virtual disk's backings should be moved to the new datastore.
        
    
    .. py:data:: VirtualMachineRelocateDiskMoveOptions.moveAllDiskBackingsAndDisallowSharing
    
        All of the virtual disk's backings should be moved to the new datastore. It is not acceptable to attach to a disk backing with the same content ID on the destination datastore. During a clone operation any delta disk backings will be consolidated.
        
    
    .. py:data:: VirtualMachineRelocateDiskMoveOptions.moveChildMostDiskBacking
    
        Move only the child-most disk backing. Any parent disk backings should be left in their current locations.
        
    