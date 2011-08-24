
================================================================================
VirtualAppSummary
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.v_app_product_info.VAppProductInfo`,
    :py:class:`~pyvisdk.do.virtual_app_v_app_state.VirtualAppVAppState`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.resource_pool_summary.ResourcePoolSummary`
    
.. class:: pyvisdk.do.virtual_app_summary.VirtualAppSummary
    
    .. py:attribute:: installBootRequired
    
        Whether one or more VMs in this vApp require a reboot to finish installation.
        
    
    .. py:attribute:: instanceUuid
    
        vCenter-specific UUID of the vApp
        
    
    .. py:attribute:: product
    
        Product information. References to properties in the URLs are expanded.
        
    
    .. py:attribute:: suspended
    
        Whether a vApp is suspended, in the process of being suspended, or in the process of being resumed. A stopped vApp is marked as suspended under the following conditions: * All child virtual machines are either suspended or powered-off. * There is at least one suspended virtual machine for which the stop action is not "suspend". If the vAppState property is "stopped", the value is set to true if the vApp is suspended (according the the above definition).
        
    
    .. py:attribute:: vAppState
    
        Whether the vApp is running
        
    