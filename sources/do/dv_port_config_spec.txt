
================================================================================
DVPortConfigSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.reconfigure_dv_port__task.ReconfigureDVPort_Task`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.dv_port_setting.DVPortSetting`,
    :py:class:`~pyvisdk.do.managed_entity.ManagedEntity`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.dv_port_config_spec.DVPortConfigSpec
    
    .. py:attribute:: configVersion
    
        The version string of the configuration.
        
    
    .. py:attribute:: description
    
        The description string of the port.
        
    
    .. py:attribute:: key
    
        The key of the port to be reconfigured.
        
    
    .. py:attribute:: name
    
        The name of the port.
        
    
    .. py:attribute:: operation
    
        The operation to remove or modify the existing ports. The valid values are: * edit * remove
        
    
    .. py:attribute:: scope
    
        The eligible entities that can connect to the port, for detail see scope.
        
    
    .. py:attribute:: setting
    
        The network setting of the port.
        
    