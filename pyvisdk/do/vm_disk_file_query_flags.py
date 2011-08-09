
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmDiskFileQueryFlags(DynamicData):
    '''Details for the virtual disk primary file.
    '''
    
    def __init__(self, capacityKb, controllerType, diskExtents, diskType, hardwareVersion, thin):
        # MUST define these
        super(VmDiskFileQueryFlags, self).__init__()
    
        self.data['capacityKb'] = capacityKb
        self.data['controllerType'] = controllerType
        self.data['diskExtents'] = diskExtents
        self.data['diskType'] = diskType
        self.data['hardwareVersion'] = hardwareVersion
        self.data['thin'] = thin
    
    
    @property
    def capacityKb(self):
        '''The flag to indicate whether the capacity of the virtual disk from the point of
        view of a virtual machine is returned.
        '''
        return self.data['capacityKb']

    @property
    def controllerType(self):
        '''The flag to indicate whether or not the controller type of the virtual disk file
        is returned.
        '''
        return self.data['controllerType']

    @property
    def diskExtents(self):
        '''The flag to indicate whether or not the disk extents of the virtual disk are
        returned.
        '''
        return self.data['diskExtents']

    @property
    def diskType(self):
        '''The flag to indicate whether the type of the physical disk backing the virtual
        disk is returned.
        '''
        return self.data['diskType']

    @property
    def hardwareVersion(self):
        '''The flag to indicate whether the hardware version of the virtual disk file is
        returned.
        '''
        return self.data['hardwareVersion']

    @property
    def thin(self):
        '''The flag to indicate whether the thin-ness of the disk is returned.
        '''
        return self.data['thin']

