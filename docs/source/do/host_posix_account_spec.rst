
================================================================================
HostPosixAccountSpec
================================================================================


.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.host_account_spec.HostAccountSpec`
    
.. class:: pyvisdk.do.host_posix_account_spec.HostPosixAccountSpec
    
    .. py:attribute:: posixId
    
        The user ID or group ID of a specified account.
        
    
    .. py:attribute:: shellAccess
    
        Grants shell access if true. By default, shell access is disallowed. As of vSphere API 4.1, this property has effect only on users with Administrator role on one or more VIM objects. For all others the default is applied.
        
    