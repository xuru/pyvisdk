
================================================================================
ScsiLun
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_multipath_info_logical_unit.HostMultipathInfoLogicalUnit`,
    :py:class:`~pyvisdk.do.host_plug_store_topology_device.HostPlugStoreTopologyDevice`,
    :py:class:`~pyvisdk.do.host_scsi_topology_lun.HostScsiTopologyLun`,
    :py:class:`~pyvisdk.do.host_storage_device_info.HostStorageDeviceInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.scsi_lun_capabilities.ScsiLunCapabilities`,
    :py:class:`~pyvisdk.do.scsi_lun_descriptor.ScsiLunDescriptor`,
    :py:class:`~pyvisdk.do.scsi_lun_durable_name.ScsiLunDurableName`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.host_device.HostDevice`
    
.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.host_scsi_disk.HostScsiDisk`
    
.. class:: pyvisdk.do.scsi_lun.ScsiLun
    
    .. py:attribute:: alternateName
    
        Alternate durable names. Records all available durable names derived from page 80h of the Vital Product Data (VPD) and the Identification Vital Product Data (VPD) page 83h as defined by the SCSI-3 Primary Commands. For devices that are not SCSI-3 compliant this property is not defined.
        
    
    .. py:attribute:: canonicalName
    
        Canonical name of the SCSI logical unit.
        
    
    .. py:attribute:: capabilities
    
        Capabilities of SCSI device.
        
    
    .. py:attribute:: descriptor
    
        List of descriptors that can be used to identify the LUN object. The uuid will also appear as a descriptor.
        
    
    .. py:attribute:: displayName
    
        User configurable display name of the SCSI logical unit. A default display name will be used if available. If the display name is not supported, it will be unset. The display name does not have to be unique but it is recommended that it be unique.
        
    
    .. py:attribute:: durableName
    
        The durable name of the SCSI device. For a SCSI-3 compliant device this property is derived from the payloads of pages 80h and 83h of the Vital Product Data (VPD) as defined by the T10 and SMI standards. For devices that do not provide this information, this property is not defined.
        
    
    .. py:attribute:: key
    
        Linkable identifier
        
    
    .. py:attribute:: lunType
    
        The type of SCSI device. Must be one of the values of ScsiLunType.
        
    
    .. py:attribute:: model
    
        The model number of the SCSI device.
        
    
    .. py:attribute:: operationalState
    
        The operational states of the LUN. When more than one item is present in the array, the first state should be considered the primary state. For example, a LUN may be "ok" and "degraded" indicating I/O is still possible to the LUN, but it is operating in a degraded mode.
        
    
    .. py:attribute:: queueDepth
    
        The queue depth of SCSI device.
        
    
    .. py:attribute:: revision
    
        The revision of the SCSI device.
        
    
    .. py:attribute:: scsiLevel
    
        The SCSI level of the SCSI device.
        
    
    .. py:attribute:: serialNumber
    
        The serial number of the SCSI device. For a device that is SCSI-3 compliant, this property is derived from page 80h of the Vital Product Data (VPD), as defined by the SCSI-3 Primary Commands (SPC-3) spec. Not all SCSI-3 compliant devices provide this information. For devices that are not SCSI-3 compliant, this property is not defined.
        
    
    .. py:attribute:: standardInquiry
    
        Standard Inquiry payload. For a SCSI-3 compliant device this property is derived from the standard inquiry data. For devices that are not SCSI-3 compliant this property is not defined.
        
    
    .. py:attribute:: uuid
    
        Universally unique identifier for the LUN used to identify ScsiLun across multiple servers.
        
    
    .. py:attribute:: vendor
    
        The vendor of the SCSI device.
        
    
    .. py:attribute:: vStorageSupport
    
        vStorage hardware acceleration support status. This property represents storage acceleration provided by the SCSI logical unit. See ScsiLunVStorageSupportStatus for valid values.
        
    