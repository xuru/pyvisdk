
================================================================================
LockerReconfiguredEvent
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.datastore_event_argument.DatastoreEventArgument`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.event.Event`
    
.. class:: pyvisdk.do.locker_reconfigured_event.LockerReconfiguredEvent
    
    .. py:attribute:: newDatastore
    
        The datastore that is now used to back the locker. This field is not set if no datastore is currently backing the locker.
        
    
    .. py:attribute:: oldDatastore
    
        The datastore that was previously backing the locker. This field is not set if a datastore was not backing the locker previously.
        
    