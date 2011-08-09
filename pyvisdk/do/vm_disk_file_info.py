
from pyvisdk.do.file_info import FileInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmDiskFileInfo(FileInfo):
    '''This data object type describes a virtual disk primary file.
    '''
    
    def __init__(self, capacityKb, controllerType, diskExtents, diskType, hardwareVersion, thin):
        # MUST define these
        super(VmDiskFileInfo, self).__init__()
    
        self.data['capacityKb'] = capacityKb
        self.data['controllerType'] = controllerType
        self.data['diskExtents'] = diskExtents
        self.data['diskType'] = diskType
        self.data['hardwareVersion'] = hardwareVersion
        self.data['thin'] = thin
    
    
    @property
    def capacityKb(self):
        '''The capacity of a virtual disk from the point of view of a virtual machine.
        '''
        return self.data['capacityKb']

    @property
    def controllerType(self):
        '''The controller type suitable for this virtual disk.
        '''
        return self.data['controllerType']

    @property
    def diskExtents(self):
        '''The extents of this virtual disk specified in absolute DS paths
        '''
        return self.data['diskExtents']

    @property
    def diskType(self):
        '''Disk type of the virtual disk.
        '''
        return self.data['diskType']

    @property
    def hardwareVersion(self):
        '''The hardware version of the virtual disk file.
        '''
        return self.data['hardwareVersion']

    @property
    def thin(self):
        '''Indicates if the disk is thin-provisioned
        '''
        return self.data['thin']

