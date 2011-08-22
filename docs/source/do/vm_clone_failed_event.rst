
================================================================================
VmCloneFailedEvent
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.folder_event_argument.FolderEventArgument`,
    :py:class:`~pyvisdk.do.host_event_argument.HostEventArgument`,
    :py:class:`~pyvisdk.do.localized_method_fault.LocalizedMethodFault`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.vm_clone_event.VmCloneEvent`
    
.. class:: pyvisdk.do.vm_clone_failed_event.VmCloneFailedEvent
    
    .. py:attribute:: destFolder
    
        The destination folder to which the virtual machine is being cloned.
        
    
    .. py:attribute:: destHost
    
        The destination host to which the virtual machine was being cloned.
        
    
    .. py:attribute:: destName
    
        The name of the destination virtual machine.
        
    
    .. py:attribute:: reason
    
        The reason why this clone operation failed.
        
    