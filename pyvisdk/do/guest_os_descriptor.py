
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class GuestOsDescriptor(DynamicData):
    '''This data object type contains information to describe a particular guest
        operating system.
    '''
    
    def __init__(self, cpuFeatureMask, family, fullName, id, recommendedColorDepth, recommendedDiskController, recommendedDiskSizeMB, recommendedEthernetCard, recommendedMemMB, recommendedSCSIController, supportedDiskControllerList, supportedEthernetCard, supportedMaxCPUs, supportedMaxMemMB, supportedMinMemMB, supportedNumDisks, supportsCpuHotAdd, supportsCpuHotRemove, supportsMemoryHotAdd, supportsSlaveDisk, supportsVMI, supportsWakeOnLan):
        # MUST define these
        super(GuestOsDescriptor, self).__init__()
    
        self.data['cpuFeatureMask'] = cpuFeatureMask
        self.data['family'] = family
        self.data['fullName'] = fullName
        self.data['id'] = id
        self.data['recommendedColorDepth'] = recommendedColorDepth
        self.data['recommendedDiskController'] = recommendedDiskController
        self.data['recommendedDiskSizeMB'] = recommendedDiskSizeMB
        self.data['recommendedEthernetCard'] = recommendedEthernetCard
        self.data['recommendedMemMB'] = recommendedMemMB
        self.data['recommendedSCSIController'] = recommendedSCSIController
        self.data['supportedDiskControllerList'] = supportedDiskControllerList
        self.data['supportedEthernetCard'] = supportedEthernetCard
        self.data['supportedMaxCPUs'] = supportedMaxCPUs
        self.data['supportedMaxMemMB'] = supportedMaxMemMB
        self.data['supportedMinMemMB'] = supportedMinMemMB
        self.data['supportedNumDisks'] = supportedNumDisks
        self.data['supportsCpuHotAdd'] = supportsCpuHotAdd
        self.data['supportsCpuHotRemove'] = supportsCpuHotRemove
        self.data['supportsMemoryHotAdd'] = supportsMemoryHotAdd
        self.data['supportsSlaveDisk'] = supportsSlaveDisk
        self.data['supportsVMI'] = supportsVMI
        self.data['supportsWakeOnLan'] = supportsWakeOnLan
    
    
    @property
    def cpuFeatureMask(self):
        '''Specifies the CPU feature compatibility masks.
        '''
        return self.data['cpuFeatureMask']

    @property
    def family(self):
        '''Family to which this guest operating system belongs.
        '''
        return self.data['family']

    @property
    def fullName(self):
        '''Full name of the guest operating system. For example, if the value of "id" is
        "win2000Pro", then the value of "fullName" is "Windows 2000 Professional".
        '''
        return self.data['fullName']

    @property
    def id(self):
        '''Identifier (short name) for the guest operating system.
        '''
        return self.data['id']

    @property
    def recommendedColorDepth(self):
        '''Recommended default color depth for this guest.
        '''
        return self.data['recommendedColorDepth']

    @property
    def recommendedDiskController(self):
        '''Recommended default disk controller type for this guest.
        '''
        return self.data['recommendedDiskController']

    @property
    def recommendedDiskSizeMB(self):
        '''Recommended default disk size for this guest, in MB.
        '''
        return self.data['recommendedDiskSizeMB']

    @property
    def recommendedEthernetCard(self):
        '''Recommended default ethernet controller type for this guest.
        '''
        return self.data['recommendedEthernetCard']

    @property
    def recommendedMemMB(self):
        '''Recommended default memory size for this guest, in MB.
        '''
        return self.data['recommendedMemMB']

    @property
    def recommendedSCSIController(self):
        '''Recommended default SCSI controller type for this guest.
        '''
        return self.data['recommendedSCSIController']

    @property
    def supportedDiskControllerList(self):
        '''List of supported disk controller types for this guest.
        '''
        return self.data['supportedDiskControllerList']

    @property
    def supportedEthernetCard(self):
        '''List of supported ethernet cards for this guest.
        '''
        return self.data['supportedEthernetCard']

    @property
    def supportedMaxCPUs(self):
        '''Maximum number of processors supported for this guest.
        '''
        return self.data['supportedMaxCPUs']

    @property
    def supportedMaxMemMB(self):
        '''Maximum memory requirements supported for this guest, in MB.
        '''
        return self.data['supportedMaxMemMB']

    @property
    def supportedMinMemMB(self):
        '''Minimum memory requirements supported for this guest, in MB.
        '''
        return self.data['supportedMinMemMB']

    @property
    def supportedNumDisks(self):
        '''Number of disks supported for this guest.
        '''
        return self.data['supportedNumDisks']

    @property
    def supportsCpuHotAdd(self):
        '''Whether virtual CPUs can be added to this guest while the virtual machine is
        running.
        '''
        return self.data['supportsCpuHotAdd']

    @property
    def supportsCpuHotRemove(self):
        '''Whether virtual CPUs can be removed from this guest while the virtual machine is
        running.
        '''
        return self.data['supportsCpuHotRemove']

    @property
    def supportsMemoryHotAdd(self):
        '''Whether the memory size for this guest can be changed while the virtual machine is
        running.
        '''
        return self.data['supportsMemoryHotAdd']

    @property
    def supportsSlaveDisk(self):
        '''Flag to indicate whether or not this guest can support a disk configured as a
        slave.
        '''
        return self.data['supportsSlaveDisk']

    @property
    def supportsVMI(self):
        '''Flag indicating whether or not this guest supports the virtual machine interface.
        '''
        return self.data['supportsVMI']

    @property
    def supportsWakeOnLan(self):
        '''Flag to indicate whether or not this guest can support Wake-on-LAN.
        '''
        return self.data['supportsWakeOnLan']

