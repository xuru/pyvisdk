
================================================================================
HostDatastoreBrowserSearchSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.search_datastore__task.SearchDatastore_Task`,
    :py:meth:`~pyvisdk.do.search_datastore_sub_folders__task.SearchDatastoreSubFolders_Task`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.file_query.FileQuery`,
    :py:class:`~pyvisdk.do.file_query_flags.FileQueryFlags`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_datastore_browser_search_spec.HostDatastoreBrowserSearchSpec
    
    .. py:attribute:: details
    
        This object comprises a set of booleans that describe what details to return for each file. The file level details apply globally to all matched files.
        
    
    .. py:attribute:: matchPattern
    
        Specifies a list of file patterns that must match for a file to be returned. This search property is a filter that applies globally so that only files matching the specified patterns are returned, regardless of the other search parameters.
        
    
    .. py:attribute:: query
    
        The set of file types to match, search criteria specific to the file type, and the amount of detail for a file. These search parameters are specific to a file type, meaning that they can be specified only if the file type to which they are associated is in the set. A file type cannot appear more than once in the set.
        
    
    .. py:attribute:: searchCaseInsensitive
    
        This flag indicates whether or not to search using a case insensitive match on type. In general the algorithm used to match file types relies on file extensions. Although the specific file extensions used are encapsulated by this API, clients are still allowed to modify the filtering behavior.
        
    
    .. py:attribute:: sortFoldersFirst
    
        By default, files are sorted in alphabetical order regardless of file type. If this flag is set to "true", folders are placed at the start of the list of results in alphabetical order. The remaining files follow in alphabetical order.
        
    