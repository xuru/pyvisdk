
================================================================================
VirtualMachineConfigOptionDescriptor
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_system.HostSystem`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_config_option_descriptor.QueryConfigOptionDescriptor`
    
.. class:: pyvisdk.do.virtual_machine_config_option_descriptor.VirtualMachineConfigOptionDescriptor
    
    .. py:attribute:: createSupported
    
        Indicates whether the associated set of configuration options can be used for virtual machine creation on a given host or cluster.
        
    
    .. py:attribute:: defaultConfigOption
    
        Indicates whether the associated set of virtual machine configuration options is the default one for a given host or cluster. If this setting is TRUE, virtual machine creates will use the associated set of configuration options, unless a config version is explicitly specified in the ConfigSpec.
        
    
    .. py:attribute:: description
    
        A description of the configOption object.
        
    
    .. py:attribute:: host
    
        List of hosts to which this descriptor applies.
        
    
    .. py:attribute:: key
    
        A unique key used to identify a configOption object in this EnvironmentBrowser.
        
    