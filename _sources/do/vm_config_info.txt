
================================================================================
VmConfigInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_machine_config_info.VirtualMachineConfigInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.v_app_ip_assignment_info.VAppIPAssignmentInfo`,
    :py:class:`~pyvisdk.do.v_app_ovf_section_info.VAppOvfSectionInfo`,
    :py:class:`~pyvisdk.do.v_app_product_info.VAppProductInfo`,
    :py:class:`~pyvisdk.do.v_app_property_info.VAppPropertyInfo`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.v_app_config_info.VAppConfigInfo`
    
.. class:: pyvisdk.do.vm_config_info.VmConfigInfo
    
    .. py:attribute:: eula
    
        End User Liceses Agreements.
        
    
    .. py:attribute:: installBootRequired
    
        Specifies whether the VM needs an initial boot before the deployment is complete.
        
    
    .. py:attribute:: installBootStopDelay
    
        Specifies the delay in seconds to wait for the VM to power off after the initial boot (used only if installBootRequired is true). A value of 0 means wait forever.
        
    
    .. py:attribute:: ipAssignment
    
        IP assignment policy and DHCP support configuration.
        
    
    .. py:attribute:: ovfEnvironmentTransport
    
        List the transports to use for properties. Supported values are: iso and com.vmware.guestInfo.
        
    
    .. py:attribute:: ovfSection
    
        List of uninterpreted OVF meta-data sections.
        
    
    .. py:attribute:: product
    
        Information about the package content.
        
    
    .. py:attribute:: property_
    
        List of properties
        
    