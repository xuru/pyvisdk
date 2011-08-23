
================================================================================
VirtualMachineSnapshotTree
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.virtual_machine_snapshot_info.VirtualMachineSnapshotInfo`,
    :py:class:`~pyvisdk.do.virtual_machine_snapshot_tree.VirtualMachineSnapshotTree`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.virtual_machine.VirtualMachine`,
    :py:class:`~pyvisdk.do.virtual_machine_power_state.VirtualMachinePowerState`,
    :py:class:`~pyvisdk.do.virtual_machine_snapshot.VirtualMachineSnapshot`,
    :py:class:`~pyvisdk.do..`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.virtual_machine_snapshot_tree.VirtualMachineSnapshotTree
    
    .. py:attribute:: backupManifest
    
        The relative path from the snapshotDirectory pointing to the backup manifest. Available for certain quiesced snapshots only.
        
    
    .. py:attribute:: childSnapshotList
    
        The snapshot data for all snapshots for which this snapshot is the parent.
        
    
    .. py:attribute:: createTime
    
        The date and time the snapshot was taken.
        
    
    .. py:attribute:: description
    
        Description of the snapshot.
        
    
    .. py:attribute:: id
    
        The unique identifier that distinguishes this snapshot from other snapshots of the virtual machine.
        
    
    .. py:attribute:: name
    
        Name of the snapshot.
        
    
    .. py:attribute:: quiesced
    
        Flag to indicate whether or not the snapshot was created with the "quiesce" option, ensuring a consistent state of the file system.
        
    
    .. py:attribute:: replaySupported
    
        Flag to indicate whether this snapshot is associated with a recording session on the virtual machine that can be replayed.
        
    
    .. py:attribute:: snapshot
    
        The managed object for this snapshot.
        
    
    .. py:attribute:: state
    
        The power state of the virtual machine when this snapshot was taken.
        
    
    .. py:attribute:: vm
    
        The virtual machine for which the snapshot was taken.
        
    