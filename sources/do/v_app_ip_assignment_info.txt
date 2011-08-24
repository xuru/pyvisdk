
================================================================================
VAppIPAssignmentInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.vm_config_info.VmConfigInfo`,
    :py:class:`~pyvisdk.do.vm_config_spec.VmConfigSpec`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.v_app_ip_assignment_info.VAppIPAssignmentInfo
    
    .. py:attribute:: ipAllocationPolicy
    
        Specifies how IP allocation should be managed by the VI platform. This is typically specified by the deployer. The set of valid options for the policy is based on the capabilities of the vApp software, as specified by the supportedAllocationSchemes property.
        
    
    .. py:attribute:: ipProtocol
    
        Specifies the chosen IP protocol for this deployment. This must be one of the values in the supportedIpProtocol field.
        
    
    .. py:attribute:: supportedAllocationScheme
    
        Specifies the IP allocation schemes supported by the guest software.
        
    
    .. py:attribute:: supportedIpProtocol
    
        Specifies the IP protocols supported by the guest software.
        
    