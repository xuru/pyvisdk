
================================================================================
VmShutdownOnIsolationEvent
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_event_argument.HostEventArgument`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.vm_powered_off_event.VmPoweredOffEvent`
    
.. class:: pyvisdk.do.vm_shutdown_on_isolation_event.VmShutdownOnIsolationEvent
    
    .. py:attribute:: isolatedHost
    
        The isolated host on which a virtual machine was shutdown.
        
    
    .. py:attribute:: shutdownResult
    
        Indicates if the shutdown was successful. If the shutdown failed, the virtual machine was powered off. see Operation
        
    