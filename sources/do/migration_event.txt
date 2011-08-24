
================================================================================
MigrationEvent
================================================================================


.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.migration_error_event.MigrationErrorEvent`,
    :py:class:`~pyvisdk.do.migration_host_error_event.MigrationHostErrorEvent`,
    :py:class:`~pyvisdk.do.migration_host_warning_event.MigrationHostWarningEvent`,
    :py:class:`~pyvisdk.do.migration_resource_error_event.MigrationResourceErrorEvent`,
    :py:class:`~pyvisdk.do.migration_resource_warning_event.MigrationResourceWarningEvent`,
    :py:class:`~pyvisdk.do.migration_warning_event.MigrationWarningEvent`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.localized_method_fault.LocalizedMethodFault`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.vm_event.VmEvent`
    
.. class:: pyvisdk.do.migration_event.MigrationEvent
    
    .. py:attribute:: fault
    
        The fault that describes the migration issue. This is typically either a MigrationFault or a VmConfigFault.
        
    