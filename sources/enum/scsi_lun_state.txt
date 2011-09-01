
==================================================================================================
ScsiLunState
==================================================================================================

.. describe:: ScsiLunState

    The Operational state of the LUN
    
    
    .. py:data:: ScsiLunState.degraded
    
        deprecated As of VI API 4.0. This state is no longer reported. One or more paths to the LUN are down, but I/O is still possible. Further path failures may result in lost connectivity.
        
    
    .. py:data:: ScsiLunState.error
    
        The LUN is dead and/or not reachable.
        
    
    .. py:data:: ScsiLunState.lostCommunication
    
        deprecated As of VI API 4.0. This state is no longer reported. No more paths are available to the LUN.
        
    
    .. py:data:: ScsiLunState.off
    
        The LUN is off. vSphere API 4.0
        
    
    .. py:data:: ScsiLunState.ok
    
        The LUN is on and available.
        
    
    .. py:data:: ScsiLunState.quiesced
    
        The LUN is inactive. vSphere API 4.0
        
    
    .. py:data:: ScsiLunState.unknownState
    
        The LUN state is unknown.
        
    