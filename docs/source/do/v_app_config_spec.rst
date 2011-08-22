
================================================================================
VAppConfigSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.create_v_app.CreateVApp`,
    :py:meth:`~pyvisdk.do.update_v_app_config.UpdateVAppConfig`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_app_import_spec.VirtualAppImportSpec`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.v_app_entity_config_info.VAppEntityConfigInfo`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.vm_config_spec.VmConfigSpec`
    
.. class:: pyvisdk.do.v_app_config_spec.VAppConfigSpec
    
    .. py:attribute:: annotation
    
        Description for the vApp.
        
    
    .. py:attribute:: entityConfig
    
        Configuration of sub-entities (virtual machine or vApp container).
        
    
    .. py:attribute:: instanceUuid
    
        vCenter-specific 128-bit UUID of a vApp, represented as a hexadecimal string. This identifier is used by vCenter to uniquely identify all vApp instances in the Virtual Infrastructure environment.
        
    