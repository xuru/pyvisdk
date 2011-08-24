
================================================================================
CustomizationSpec
================================================================================


.. describe:: Parameter to
    
    :py:meth:`~pyvisdk.do.check_customization_spec.CheckCustomizationSpec`,
    :py:meth:`~pyvisdk.do.customize_vm__task.CustomizeVM_Task`
    
.. describe:: Property of
    
    :py:class:`~pyvisdk.do.customization_spec_item.CustomizationSpecItem`,
    :py:class:`~pyvisdk.do.virtual_machine_clone_spec.VirtualMachineCloneSpec`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.customization_adapter_mapping.CustomizationAdapterMapping`,
    :py:class:`~pyvisdk.do.customization_global_ip_settings.CustomizationGlobalIPSettings`,
    :py:class:`~pyvisdk.do.customization_identity_settings.CustomizationIdentitySettings`,
    :py:class:`~pyvisdk.do.customization_options.CustomizationOptions`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.customization_spec.CustomizationSpec
    
    .. py:attribute:: encryptionKey
    
        Byte array containing the public key used to encrypt any passwords stored in the specification. Both the client and the server can use this to determine if stored passwords can be decrypted by the server or if the passwords need to be re-entered and re-encrypted before the specification can be used.
        
    
    .. py:attribute:: globalIPSettings
    
        Global IP settings constitute the IP settings that are not specific to a particular virtual network adapter.
        
    
    .. py:attribute:: identity
    
        Network identity and settings, similar to Microsoft's Sysprep tool. This is a Sysprep, LinuxPrep, or SysprepText object.
        
    
    .. py:attribute:: nicSettingMap
    
        IP settings that are specific to a particular virtual network adapter. The AdapterMapping object maps a network adapter's MAC address to its Adapter settings object. May be empty if there are no network adapters, else should match number of network adapters in the VM.
        
    
    .. py:attribute:: options
    
        Optional operations (either LinuxOptions or WinOptions).
        
    