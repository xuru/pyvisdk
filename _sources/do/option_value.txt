
================================================================================
OptionValue
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.power_on_multi_vm__task.PowerOnMultiVM_Task`,
    :py:meth:`~pyvisdk.do.update_options.UpdateOptions`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.cluster_das_config_info.ClusterDasConfigInfo`,
    :py:class:`~pyvisdk.do.cluster_dpm_config_info.ClusterDpmConfigInfo`,
    :py:class:`~pyvisdk.do.cluster_drs_config_info.ClusterDrsConfigInfo`,
    :py:class:`~pyvisdk.do.host_config_info.HostConfigInfo`,
    :py:class:`~pyvisdk.do.host_config_spec.HostConfigSpec`,
    :py:class:`~pyvisdk.do.option_manager.OptionManager`,
    :py:class:`~pyvisdk.do.virtual_machine_config_info.VirtualMachineConfigInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_config_spec.VirtualMachineConfigSpec`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.host_internet_scsi_hba_param_value.HostInternetScsiHbaParamValue`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_options.QueryOptions`
    
.. class:: pyvisdk.do.option_value.OptionValue
    
    .. py:attribute:: key
    
        The name of the option using dot notation to reflect the option's position in a hierarchy. For example, you might have an option called "Ethernet" and another option that is a child of that called "Connection". In this case, the key for the latter could be defined as "Ethernet.Connection"
        
    
    .. py:attribute:: value
    
        The value of the option. The Any data object type enables you to define any value for the option. Typically, however, the value of an option is of type String or Integer.
        
    