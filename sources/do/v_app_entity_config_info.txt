
================================================================================
VAppEntityConfigInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.import_spec.ImportSpec`,
    :py:class:`~pyvisdk.do.v_app_config_info.VAppConfigInfo`,
    :py:class:`~pyvisdk.do.v_app_config_spec.VAppConfigSpec`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.managed_entity.ManagedEntity`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.v_app_entity_config_info.VAppEntityConfigInfo
    
    .. py:attribute:: destroyWithParent
    
        Whether the entity should be removed, when this vApp is removed. This is only set for linked children.
        
    
    .. py:attribute:: key
    
        Entity to power on or power off. This can be a virtual machine or a vApp.
        
    
    .. py:attribute:: startAction
    
        How to start the entity. Valid settings are none or powerOn. If set to none, then the entity does not participate in auto-start.
        
    
    .. py:attribute:: startDelay
    
        Delay in seconds before continuing with the next entity in the order of entities to be started.
        
    
    .. py:attribute:: startOrder
    
        Specifies the start order for this entity. Entities are started from lower numbers to higher-numbers and reverse on shutdown. Multiple entities with the same start-order can be started in parallel and the order is unspecified. This value must be 0 or higher.
        
    
    .. py:attribute:: stopAction
    
        Defines the stop action for the entity. Can be set to none, powerOff, guestShutdown, or suspend. If set to none, then the entity does not participate in auto-stop.
        
    
    .. py:attribute:: stopDelay
    
        Delay in seconds before continuing with the next entity in the order sequence. This is only used if the stopAction is guestShutdown.
        
    
    .. py:attribute:: tag
    
        Tag for entity.
        
    
    .. py:attribute:: waitingForGuest
    
        Determines if the virtual machine should start after receiving a heartbeat, from the guest. When a virtual machine is next in the start order, the system either waits a specified period of time for a virtual machine to power on or it waits until it receives a successful heartbeat from a powered on virtual machine. By default, this is set to false.
        
    