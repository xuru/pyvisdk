
================================================================================
HostInternetScsiHbaParamValue
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.update_internet_scsi_advanced_options.UpdateInternetScsiAdvancedOptions`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_internet_scsi_hba.HostInternetScsiHba`,
    :py:class:`~pyvisdk.do.host_internet_scsi_hba_send_target.HostInternetScsiHbaSendTarget`,
    :py:class:`~pyvisdk.do.host_internet_scsi_hba_static_target.HostInternetScsiHbaStaticTarget`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.option_value.OptionValue`
    
.. class:: pyvisdk.do.host_internet_scsi_hba_param_value.HostInternetScsiHbaParamValue
    
    .. py:attribute:: isInherited
    
        Indicates if the value is inherited from some other source. If unset, the value is not inheritable. isInherited can be modified only if it has already been set. If value is to being modified, isInherited should be set to true. Setting isInherited to false will result in the value being once again inherited from the source.
        
    