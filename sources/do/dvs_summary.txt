
================================================================================
DVSSummary
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.distributed_virtual_switch.DistributedVirtualSwitch`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.distributed_virtual_switch_product_spec.DistributedVirtualSwitchProductSpec`,
    :py:class:`~pyvisdk.do.dvs_contact_info.DVSContactInfo`,
    :py:class:`~pyvisdk.do.host_system.HostSystem`,
    :py:class:`~pyvisdk.do.virtual_machine.VirtualMachine`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.dvs_summary.DVSSummary
    
    .. py:attribute:: contact
    
        The human operator contact information.
        
    
    .. py:attribute:: description
    
        A description string of the switch.
        
    
    .. py:attribute:: host
    
        The hosts with vNICs that connect to the switch.
        
    
    .. py:attribute:: hostMember
    
        The names of the hosts that join the switch.
        
    
    .. py:attribute:: name
    
        The name of the switch.
        
    
    .. py:attribute:: numPorts
    
        Current number of ports, not including conflict ports.
        
    
    .. py:attribute:: portgroupName
    
        The names of the portgroups that are defined on the switch.
        
    
    .. py:attribute:: productInfo
    
        The product information for the implementation of the switch.
        
    
    .. py:attribute:: uuid
    
        The generated UUID of the switch.
        
    
    .. py:attribute:: vm
    
        The Virtual Machines with vNICs that connect to the switch.
        
    