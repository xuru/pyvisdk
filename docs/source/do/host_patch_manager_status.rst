
================================================================================
HostPatchManagerStatus
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_patch_manager_result.HostPatchManagerResult`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_patch_manager_status_prerequisite_patch.HostPatchManagerStatusPrerequisitePatch`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.scan_host_patch__task.ScanHostPatch_Task`
    
.. class:: pyvisdk.do.host_patch_manager_status.HostPatchManagerStatus
    
    .. py:attribute:: applicable
    
        Whether or not this update is applicable to this host. An update may not be applicable to the ESX host for many reasons--for example, it is obsolete, it conflicts with other installed patches or libraries, and so on. The reason shows some of the reasons why the update is not applicable. An update could be inapplicable with no reason listed. This is because the prerequisite install state is not correct. For example, update A is one of the prerequisites of update B. B not only requires A to be installed, but also requires the host is rebooted after A is installed. When A is installed and the host has not been restarted after the installation, B will not be applicable. In such a case, the scan on both updates A and B would yield a whole picture of the update applicable status.
        
    
    .. py:attribute:: id
    
        Unique identifier for this update.
        
    
    .. py:attribute:: installed
    
        Whether the update is installed on the server.
        
    
    .. py:attribute:: installState
    
        The installation state of the update. Unset if the update is not installed on the server.See HostPatchManagerInstallState
        
    
    .. py:attribute:: integrity
    
        The integrity status of the update's metadata. The value would be unset if the integrity status is unknown to the server.See HostPatchManagerIntegrityStatus
        
    
    .. py:attribute:: prerequisitePatch
    
        Prerequisite update.
        
    
    .. py:attribute:: reason
    
        Possible reasons why an update is not applicable to the ESX host.See HostPatchManagerReason
        
    
    .. py:attribute:: reconnectRequired
    
        Whether or not this update requires caller to reconnect to the host. This is usually because the update is on the agent that running on the host, the agent would thus be restarted when the update is applied. Caller can reconnect (and possibly relogin) to the host after the agent has been restarted.
        
    
    .. py:attribute:: restartRequired
    
        Whether or not this update requires a host restart to take effect.
        
    
    .. py:attribute:: supersededPatchIds
    
        Patches that are superseded by this update.
        
    
    .. py:attribute:: vmOffRequired
    
        Whether or not this update requires the host in maintenance mode.
        
    