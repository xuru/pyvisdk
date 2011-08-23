
================================================================================
HostIpmiInfo
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.update_ipmi.UpdateIpmi`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_config_info.HostConfigInfo`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_ipmi_info.HostIpmiInfo
    
    .. py:attribute:: bmcIpAddress
    
        IP address of the BMC on the host. It should be null terminated.
        
    
    .. py:attribute:: bmcMacAddress
    
        MAC address of the BMC on the host. The MAC address should be of the form xx:xx:xx:xx:xx:xx where each x is a hex digit. It should be null terminated.
        
    
    .. py:attribute:: login
    
        User ID for logging into the BMC. BMC usernames may be up to 16 characters and must be null terminated. Hence, a login comprises 17 or fewer characters.
        
    
    .. py:attribute:: password
    
        Password for logging into the BMC. Only used for configuration, returned as unset while reading. The password can be up to 16 characters and must be null terminated. Hence, a password comprises 17 or fewer characters.
        
    