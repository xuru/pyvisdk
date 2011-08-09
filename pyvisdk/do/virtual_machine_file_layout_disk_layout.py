
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineFileLayoutDiskLayout(DynamicData):
    '''Enumerats the set of files for each virtual disk.
    '''
    
    def __init__(self, diskFile, key):
        # MUST define these
        super(VirtualMachineFileLayoutDiskLayout, self).__init__()
    
        self.data['diskFile'] = diskFile
        self.data['key'] = key
    
    
    @property
    def diskFile(self):
        '''List of files that makes up the virtual disk. At least one entry always exists in
        this array. The first entry is the main descriptor of the virtual disk
        (the one used when adding the disk to a virtual machine). These are
        complete datastore paths, not relative paths.
        '''
        return self.data['diskFile']

    @property
    def key(self):
        '''Identification of the disk in config.
        '''
        return self.data['key']

