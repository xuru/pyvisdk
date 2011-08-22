
================================================================================
DiagnosticManagerLogDescriptor
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.description.Description`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_descriptions.QueryDescriptions`
    
.. class:: pyvisdk.do.diagnostic_manager_log_descriptor.DiagnosticManagerLogDescriptor
    
    .. py:attribute:: creator
    
        The application that generated the log file. For more information on currently supported creators, see DiagnosticManagerLogCreator.
        
    
    .. py:attribute:: fileName
    
        The filename of the log.
        
    
    .. py:attribute:: format
    
        Describes the format of the log file. For more information on currently supported formats, see DiagnosticManagerLogFormat.
        
    
    .. py:attribute:: info
    
        Localized description of log file.
        
    
    .. py:attribute:: key
    
        A key to identify the log file for browsing and download operations.
        
    
    .. py:attribute:: mimeType
    
        Describes the mime-type of the returned file. Typical mime-types include: * text/plain - for a plain log file
        
    