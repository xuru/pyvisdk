
==================================================================================================
VAppCloneSpecProvisioningType
==================================================================================================

.. describe:: VAppCloneSpecProvisioningType

    The cloned VMs can either be provisioned the same way as the VMs they are a clone of, thin provisioned or thick provisioned, or linked clones (i.e., using delta disks).
    
    
    .. py:data:: VAppCloneSpecProvisioningType.sameAsSource
    
        Each disk in the cloned virtual machines will have the same type of disk as the source vApp.
        
    
    .. py:data:: VAppCloneSpecProvisioningType.thick
    
        Each disk in the cloned virtual machines are allocated and committed in full size immediately.
        
    
    .. py:data:: VAppCloneSpecProvisioningType.thin
    
        Each disk in the cloned virtual machines is allocated in full size now and committed on demand. This is only supported on VMFS-3 and newer datastores. Other types of datastores may create thick disks.
        
    