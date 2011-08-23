
================================================================================
VmWwnConflictEvent
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_event_argument.HostEventArgument`,
    :py:class:`~pyvisdk.do.vm_event_argument.VmEventArgument`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.vm_event.VmEvent`
    
.. class:: pyvisdk.do.vm_wwn_conflict_event.VmWwnConflictEvent
    
    .. py:attribute:: conflictedHosts
    
        The host whose physical WWN conflicts with the current virtual machine's WWN.
        
    
    .. py:attribute:: conflictedVms
    
        The virtual machine whose WWN conflicts with the current virtual machine's WWN.
        
    
    .. py:attribute:: wwn
    
        The WWN in conflict.
        
    