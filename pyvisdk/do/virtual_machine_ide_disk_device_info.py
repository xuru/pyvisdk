
from pyvisdk.do.virtual_machine_disk_device_info import VirtualMachineDiskDeviceInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineIdeDiskDeviceInfo(VirtualMachineDiskDeviceInfo):
    '''The IdeDiskDeviceInfo class contains detailed information about a specific IDE
        disk hardware device. These devices are for the
        vim.vm.device.VirtualDisk.RawDiskVer2BackingInfo and
        vim.vm.device.VirtualDisk.PartitionedRawDiskVer2BackingInfo backings.
    '''
    
    def __init__(self, partitionTable):
        # MUST define these
        super(VirtualMachineIdeDiskDeviceInfo, self).__init__()
    
        self.data['partitionTable'] = partitionTable
    
    
    @property
    def partitionTable(self):
        '''
        '''
        return self.data['partitionTable']

