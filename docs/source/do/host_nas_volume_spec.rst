
================================================================================
HostNasVolumeSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.create_nas_datastore.CreateNasDatastore`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_nas_volume_config.HostNasVolumeConfig`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_nas_volume_spec.HostNasVolumeSpec
    
    .. py:attribute:: accessMode
    
        Access mode for the mount point.
        
    
    .. py:attribute:: localPath
    
        The localPath refers to the name of the NAS datastore to be created using this specification.
        
    
    .. py:attribute:: password
    
        If type is CIFS, the password to use when connecting to the CIFS server. If type is NFS, this field will be ignored.
        
    
    .. py:attribute:: remoteHost
    
        The host that runs the NFS server.
        
    
    .. py:attribute:: remotePath
    
        The remote path of the NFS mount point.
        
    
    .. py:attribute:: type
    
        The type of the the NAS volume (CIFS / NFS). If not specified, defaults to nfs.
        
    
    .. py:attribute:: userName
    
        If type is CIFS, the user name to use when connecting to the CIFS server. If type is NFS, this field will be ignored.
        
    