
================================================================================
HostInternetScsiHbaSendTarget
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.add_internet_scsi_send_targets.AddInternetScsiSendTargets`,
    :py:meth:`~pyvisdk.do.remove_internet_scsi_send_targets.RemoveInternetScsiSendTargets`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_internet_scsi_hba.HostInternetScsiHba`,
    :py:class:`~pyvisdk.do.host_internet_scsi_hba_target_set.HostInternetScsiHbaTargetSet`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_internet_scsi_hba_authentication_properties.HostInternetScsiHbaAuthenticationProperties`,
    :py:class:`~pyvisdk.do.host_internet_scsi_hba_digest_properties.HostInternetScsiHbaDigestProperties`,
    :py:class:`~pyvisdk.do.host_internet_scsi_hba_param_value.HostInternetScsiHbaParamValue`,
    :py:class:`~pyvisdk.do.option_def.OptionDef`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_internet_scsi_hba_send_target.HostInternetScsiHbaSendTarget
    
    .. py:attribute:: address
    
        The IP address or hostname of the storage device.
        
    
    .. py:attribute:: advancedOptions
    
        A list of the current options settings for the host bus adapter.
        
    
    .. py:attribute:: authenticationProperties
    
        The authentication settings for this discovery target. All static targets discovered via this target will inherit the use of these settings unless the static target's authentication settings are explicitly set.
        
    
    .. py:attribute:: digestProperties
    
        The digest settings for this discovery target. All static targets discovered via this target will inherit the use of these settings unless the static target's digest settings are explicitly set.
        
    
    .. py:attribute:: parent
    
        The device name of the host bus adapter from which settings can be inherited.
        
    
    .. py:attribute:: port
    
        The TCP port of the storage device. If not specified, the standard default of 3260 is used.
        
    
    .. py:attribute:: supportedAdvancedOptions
    
        A list of supported key/value pair advanced options for the host bus adapter including their type information.
        
    