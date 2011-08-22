
================================================================================
LocalizationManagerMessageCatalog
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.localization_manager.LocalizationManager`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.localization_manager_message_catalog.LocalizationManagerMessageCatalog
    
    .. py:attribute:: catalogName
    
        The name of the catalog.
        
    
    .. py:attribute:: catalogUri
    
        The URI (relative to the connection URL for the VirtualCenter server itself) from which the catalog can be downloaded. The caller will need to augment this with a scheme and authority (host and port) to make a complete URL.
        
    
    .. py:attribute:: lastModified
    
        The last-modified time of the catalog file, if available
        
    
    .. py:attribute:: locale
    
        The locale for the catalog.
        
    
    .. py:attribute:: md5sum
    
        The checksum of the catalog file, if available
        
    
    .. py:attribute:: moduleName
    
        The module or extension that publishes this catalog. The moduleName will be empty for the core catalogs for the VirtualCenter server itself.
        
    