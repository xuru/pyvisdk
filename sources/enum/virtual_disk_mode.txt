
==================================================================================================
VirtualDiskMode
==================================================================================================

.. describe:: VirtualDiskMode

    The list of known disk modes.The list of supported disk modes varies by the backing type. The "persistent" mode is supported by every backing type.
    
    
    .. py:data:: VirtualDiskMode.append
    
        Changes are appended to the redo log; you revoke changes by removing the undo log.
        
    
    .. py:data:: VirtualDiskMode.independent_nonpersistent
    
        Same as nonpersistent, but not affected by snapshots.
        
    
    .. py:data:: VirtualDiskMode.independent_persistent
    
        Same as persistent, but not affected by snapshots.
        
    
    .. py:data:: VirtualDiskMode.nonpersistent
    
        Changes to virtual disk are made to a redo log and discarded at power off.
        
    
    .. py:data:: VirtualDiskMode.persistent
    
        Changes are immediately and permanently written to the virtual disk.
        
    
    .. py:data:: VirtualDiskMode.undoable
    
        Changes are made to a redo log, but you are given the option to commit or undo.
        
    