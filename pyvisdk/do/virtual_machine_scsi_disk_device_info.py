
from pyvisdk.do.virtual_machine_disk_device_info import VirtualMachineDiskDeviceInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineScsiDiskDeviceInfo(VirtualMachineDiskDeviceInfo):
    '''The ScsiDiskDeviceInfo class contains detailed information about a specific scsi
        disk hardware device. These devices are for the
        vim.vm.device.VirtualDisk.RawDiskMappingVer1BackingInfo.
    '''
    
    def __init__(self, disk, lunNumber, transportHint):
        # MUST define these
        super(VirtualMachineScsiDiskDeviceInfo, self).__init__()
    
        self.data['disk'] = disk
        self.data['lunNumber'] = lunNumber
        self.data['transportHint'] = transportHint
    
    
    @property
    def disk(self):
        '''Detailed information about the disk.
        '''
        return self.data['disk']

    @property
    def lunNumber(self):
        '''LUN number hint used to identify the SCSI device. To definitively correlate this
        device with a host physical disk, use the disk property. This identifier
        is intended as a hint to end users to identify the disk device.
        '''
        return self.data['lunNumber']

    @property
    def transportHint(self):
        '''Transport identifier hint used to identify the device. To definitively correlate
        this device with a host physical disk, use the disk property. This
        identifier is intended as a hint to end users to identify the disk device.
        '''
        return self.data['transportHint']

