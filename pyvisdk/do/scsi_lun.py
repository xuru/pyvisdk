
from pyvisdk.do.host_device import HostDevice
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ScsiLun(HostDevice):
    '''The ScsiLun data object describes a SCSI logical unit. A SCSI logical unit is a
        host device that an ESX Server or virtual machine can use for I/O
        operations.An ESX Server creates SCSI logical unit objects to represent
        devices in the host configuration. (See the definition of ScsiLunType for
        a list of the supported device types.) The vSphere API uses one of two
        object types to represent a SCSI logical unit, depending on the device
        type.* Disks containing file system volumes or parts of volumes for hosts
        or raw disks for virtual machines. To represent disks, the ESX Server
        creates a HostScsiDisk object, which inherits properties from the ScsiLun
        base class. * Other SCSI devices, for example SCSI passthrough devices for
        virtual machines. To represent one of these devices, the ESX Server
        creates a ScsiLun object.When the Server creates a HostScsiDisk or ScsiLun
        object, it specifies a valid device name and type:* deviceName - A string
        representing the name of the device that is meaningful to the host. The
        following are some examples of device names.    * deviceType - A string
        describing the type of device. The following are some examples of device
        types.
    '''
    
    def __init__(self, alternateName, canonicalName, capabilities, descriptor, displayName, durableName, key, lunType, model, operationalState, queueDepth, revision, scsiLevel, serialNumber, standardInquiry, uuid, vendor, vStorageSupport):
        # MUST define these
        super(ScsiLun, self).__init__()
    
        self.data['alternateName'] = alternateName
        self.data['canonicalName'] = canonicalName
        self.data['capabilities'] = capabilities
        self.data['descriptor'] = descriptor
        self.data['displayName'] = displayName
        self.data['durableName'] = durableName
        self.data['key'] = key
        self.data['lunType'] = lunType
        self.data['model'] = model
        self.data['operationalState'] = operationalState
        self.data['queueDepth'] = queueDepth
        self.data['revision'] = revision
        self.data['scsiLevel'] = scsiLevel
        self.data['serialNumber'] = serialNumber
        self.data['standardInquiry'] = standardInquiry
        self.data['uuid'] = uuid
        self.data['vendor'] = vendor
        self.data['vStorageSupport'] = vStorageSupport
    
    
    @property
    def alternateName(self):
        '''Alternate durable names. Records all available durable names derived from page 80h
        of the Vital Product Data (VPD) and the Identification Vital Product Data
        (VPD) page 83h as defined by the SCSI-3 Primary Commands. For devices that
        are not SCSI-3 compliant this property is not defined.
        '''
        return self.data['alternateName']

    @property
    def canonicalName(self):
        '''Canonical name of the SCSI logical unit.
        '''
        return self.data['canonicalName']

    @property
    def capabilities(self):
        '''Capabilities of SCSI device.
        '''
        return self.data['capabilities']

    @property
    def descriptor(self):
        '''List of descriptors that can be used to identify the LUN object. The uuid will
        also appear as a descriptor.
        '''
        return self.data['descriptor']

    @property
    def displayName(self):
        '''User configurable display name of the SCSI logical unit. A default display name
        will be used if available. If the display name is not supported, it will
        be unset. The display name does not have to be unique but it is
        recommended that it be unique.
        '''
        return self.data['displayName']

    @property
    def durableName(self):
        '''The durable name of the SCSI device. For a SCSI-3 compliant device this property
        is derived from the payloads of pages 80h and 83h of the Vital Product
        Data (VPD) as defined by the T10 and SMI standards. For devices that do
        not provide this information, this property is not defined.
        '''
        return self.data['durableName']

    @property
    def key(self):
        '''Linkable identifier
        '''
        return self.data['key']

    @property
    def lunType(self):
        '''The type of SCSI device. Must be one of the values of ScsiLunType.
        '''
        return self.data['lunType']

    @property
    def model(self):
        '''The model number of the SCSI device.
        '''
        return self.data['model']

    @property
    def operationalState(self):
        '''The operational states of the LUN. When more than one item is present in the
        array, the first state should be considered the primary state. For
        example, a LUN may be "ok" and "degraded" indicating I/O is still possible
        to the LUN, but it is operating in a degraded mode.
        '''
        return self.data['operationalState']

    @property
    def queueDepth(self):
        '''The queue depth of SCSI device.
        '''
        return self.data['queueDepth']

    @property
    def revision(self):
        '''The revision of the SCSI device.
        '''
        return self.data['revision']

    @property
    def scsiLevel(self):
        '''The SCSI level of the SCSI device.
        '''
        return self.data['scsiLevel']

    @property
    def serialNumber(self):
        '''The serial number of the SCSI device. For a device that is SCSI-3 compliant, this
        property is derived from page 80h of the Vital Product Data (VPD), as
        defined by the SCSI-3 Primary Commands (SPC-3) spec. Not all SCSI-3
        compliant devices provide this information. For devices that are not
        SCSI-3 compliant, this property is not defined.
        '''
        return self.data['serialNumber']

    @property
    def standardInquiry(self):
        '''Standard Inquiry payload. For a SCSI-3 compliant device this property is derived
        from the standard inquiry data. For devices that are not SCSI-3 compliant
        this property is not defined.
        '''
        return self.data['standardInquiry']

    @property
    def uuid(self):
        '''Universally unique identifier for the LUN used to identify ScsiLun across multiple
        servers.
        '''
        return self.data['uuid']

    @property
    def vendor(self):
        '''The vendor of the SCSI device.
        '''
        return self.data['vendor']

    @property
    def vStorageSupport(self):
        '''vStorage hardware acceleration support status. This property represents storage
        acceleration provided by the SCSI logical unit. See
        ScsiLunVStorageSupportStatus for valid values.
        '''
        return self.data['vStorageSupport']

