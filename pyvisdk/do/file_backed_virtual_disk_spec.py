
from pyvisdk.do.virtual_disk_spec import VirtualDiskSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class FileBackedVirtualDiskSpec(VirtualDiskSpec):
    '''Specification used to create a file based virtual disk
    '''
    
    def __init__(self, capacityKb):
        # MUST define these
        super(FileBackedVirtualDiskSpec, self).__init__()
    
        self.data['capacityKb'] = capacityKb
    
    
    @property
    def capacityKb(self):
        '''Specify the capacity of the virtual disk in Kb.
        '''
        return self.data['capacityKb']

