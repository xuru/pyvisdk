
================================================================================
UserSearchResult
================================================================================


.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.posix_user_search_result.PosixUserSearchResult`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.retrieve_user_groups.RetrieveUserGroups`
    
.. class:: pyvisdk.do.user_search_result.UserSearchResult
    
    .. py:attribute:: fullName
    
        Full name of the user found by the search, or the description of a group, if available.
        
    
    .. py:attribute:: group
    
        If this is true, then the result is a group. If this is false, then the result is a user.
        
    
    .. py:attribute:: principal
    
        Login name of a user or the name of a group. This key is the user within the searched domain.
        
    