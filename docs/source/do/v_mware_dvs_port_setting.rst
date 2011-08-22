
================================================================================
VMwareDVSPortSetting
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.bool_policy.BoolPolicy`,
    :py:class:`~pyvisdk.do.dvs_security_policy.DVSSecurityPolicy`,
    :py:class:`~pyvisdk.do.int_policy.IntPolicy`,
    :py:class:`~pyvisdk.do.vmware_distributed_virtual_switch_vlan_spec.VmwareDistributedVirtualSwitchVlanSpec`,
    :py:class:`~pyvisdk.do.vmware_uplink_port_teaming_policy.VmwareUplinkPortTeamingPolicy`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dv_port_setting.DVPortSetting`
    
.. class:: pyvisdk.do.v_mware_dvs_port_setting.VMwareDVSPortSetting
    
    .. py:attribute:: qosTag
    
        This property is currently not supported.
        
    
    .. py:attribute:: securityPolicy
    
        The security policy.
        
    
    .. py:attribute:: txUplink
    
        Whether this should forward all incoming traffic out an uplink
        
    
    .. py:attribute:: uplinkTeamingPolicy
    
        The uplink teaming policy. This property is ignored for uplink ports.
        
    
    .. py:attribute:: vlan
    
        The VLAN Specification of the port.
        
    