
================================================================================
UserSession
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.session_manager.SessionManager`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.clone_session.CloneSession`,
    :py:meth:`~pyvisdk.do.impersonate_user.ImpersonateUser`,
    :py:meth:`~pyvisdk.do.login.Login`,
    :py:meth:`~pyvisdk.do.login_by_sspi.LoginBySSPI`,
    :py:meth:`~pyvisdk.do.login_extension_by_certificate.LoginExtensionByCertificate`,
    :py:meth:`~pyvisdk.do.login_extension_by_subject_name.LoginExtensionBySubjectName`
    
.. class:: pyvisdk.do.user_session.UserSession
    
    .. py:attribute:: fullName
    
        The full name of the user, if available.
        
    
    .. py:attribute:: key
    
        A unique identifier for this session, also known as the session ID.
        
    
    .. py:attribute:: lastActiveTime
    
        Timestamp when the user last executed a command.
        
    
    .. py:attribute:: locale
    
        The locale for the session used for data formatting and preferred for messages.
        
    
    .. py:attribute:: loginTime
    
        Timestamp when the user last logged on to the server.
        
    
    .. py:attribute:: messageLocale
    
        The locale used for messages for the session. If there are no localized messages for the user-specified locale, then the server determines this locale.
        
    
    .. py:attribute:: userName
    
        The user name represented by this session.
        
    