
==================================================================================================
OvfCreateImportSpecParamsDiskProvisioningType
==================================================================================================

.. describe:: OvfCreateImportSpecParamsDiskProvisioningType

    Types of disk provisioning that can be set for the disk in the deployed OVF package.
    
    
    .. py:data:: OvfCreateImportSpecParamsDiskProvisioningType.flat
    
        Depending on the host type, Flat is mapped to either MonolithicFlat or Thick.
        
    
    .. py:data:: OvfCreateImportSpecParamsDiskProvisioningType.monolithicFlat
    
        Flat VMDK format with embedded descriptor. Data is pre-allocated.
        
    
    .. py:data:: OvfCreateImportSpecParamsDiskProvisioningType.monolithicSparse
    
        Sparse VMDK format with embedded descriptor. Data is not pre-allocated.
        
    
    .. py:data:: OvfCreateImportSpecParamsDiskProvisioningType.sparse
    
        Depending on the host type, Sparse is mapped to either MonolithicSparse or Thin.
        
    
    .. py:data:: OvfCreateImportSpecParamsDiskProvisioningType.thick
    
        Flat VMDK format. Data is pre-allocated.
        
    
    .. py:data:: OvfCreateImportSpecParamsDiskProvisioningType.thin
    
        Sparse VMDK format. Data is not pre-allocated.
        
    
    .. py:data:: OvfCreateImportSpecParamsDiskProvisioningType.twoGbMaxExtentFlat
    
        Flat VMDK format where each extent is limited to 2Gb. Data is pre-allocated.
        
    
    .. py:data:: OvfCreateImportSpecParamsDiskProvisioningType.twoGbMaxExtentSparse
    
        Sparse VMDK format where each extent is limited to 2Gb. Data is not pre-allocated.
        
    