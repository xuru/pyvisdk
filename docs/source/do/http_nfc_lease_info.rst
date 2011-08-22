
================================================================================
HttpNfcLeaseInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.http_nfc_lease.HttpNfcLease`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.http_nfc_lease.HttpNfcLease`,
    :py:class:`~pyvisdk.do.http_nfc_lease_datastore_lease_info.HttpNfcLeaseDatastoreLeaseInfo`,
    :py:class:`~pyvisdk.do.http_nfc_lease_device_url.HttpNfcLeaseDeviceUrl`,
    :py:class:`~pyvisdk.do.managed_entity.ManagedEntity`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.http_nfc_lease_info.HttpNfcLeaseInfo
    
    .. py:attribute:: deviceUrl
    
        The deviceUrl property contains a mapping from logical device keys to URLs.
        
    
    .. py:attribute:: entity
    
        The VirtualMachine or VirtualApp this lease covers.
        
    
    .. py:attribute:: hostMap
    
        Map of URLs for leased hosts for a given datastore. This is used to look up multi-POST-capable hosts for a datastore.
        
    
    .. py:attribute:: lease
    
        The HttpNfcLease object this information belongs to.
        
    
    .. py:attribute:: leaseTimeout
    
        Number of seconds before the lease times out. The client extends the lease by calling HttpNfcLeaseProgress before the timeout has expired.
        
    
    .. py:attribute:: totalDiskCapacityInKB
    
        Total capacity in kilobytes of all disks in all Virtual Machines covered by this lease. This can be used to track progress when transferring disks.
        
    