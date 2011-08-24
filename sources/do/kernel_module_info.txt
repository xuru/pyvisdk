
================================================================================
KernelModuleInfo
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.kernel_module_section_info.KernelModuleSectionInfo`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. describe:: Returned by
    
    :py:meth:`~pyvisdk.do.query_modules.QueryModules`
    
.. class:: pyvisdk.do.kernel_module_info.KernelModuleInfo
    
    .. py:attribute:: bssSection
    
        BSS section information.
        
    
    .. py:attribute:: dataSection
    
        Data section information.
        
    
    .. py:attribute:: enabled
    
        Is the module enabled?
        
    
    .. py:attribute:: filename
    
        Module filename, without the path.
        
    
    .. py:attribute:: id
    
        Module ID.
        
    
    .. py:attribute:: loaded
    
        Is the module loaded?
        
    
    .. py:attribute:: name
    
        Module name.
        
    
    .. py:attribute:: optionString
    
        Option string configured to be passed to the kernel module when loaded. Note that this is not necessarily the option string currently in use by the kernel module.
        
    
    .. py:attribute:: readOnlySection
    
        Read-only section information.
        
    
    .. py:attribute:: textSection
    
        Text section information.
        
    
    .. py:attribute:: useCount
    
        Number of references to this module.
        
    
    .. py:attribute:: version
    
        Version string.
        
    
    .. py:attribute:: writableSection
    
        Writable section information.
        
    