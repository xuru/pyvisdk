
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineFileLayoutExDiskLayout(DynamicData):
    '''Layout of a virtual disk, including the base- and delta- disks.A virtual disk
        typically is made up of a chain of disk-units.
    '''
    
    def __init__(self, chain, key):
        # MUST define these
        super(VirtualMachineFileLayoutExDiskLayout, self).__init__()
    
        self.data['chain'] = chain
        self.data['key'] = key
    
    
    @property
    def chain(self):
        '''The disk-unit chain that makes up this virtual disk.
        '''
        return self.data['chain']

    @property
    def key(self):
        '''Identifier for the virtual disk in device.
        '''
        return self.data['key']

