
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDiskDimensionsLba(DynamicData):
    '''This data object type describes the logical block addressing system that uses
        block numbers and block sizes to refer to a block. This scheme is employed
        by SCSI. If a SCSI disk is not involved, then blockSize is 512 bytes.
    '''
    
    def __init__(self, block, blockSize):
        # MUST define these
        super(HostDiskDimensionsLba, self).__init__()
    
        self.data['block'] = block
        self.data['blockSize'] = blockSize
    
    
    @property
    def block(self):
        '''The number of blocks.
        '''
        return self.data['block']

    @property
    def blockSize(self):
        '''The size of the blocks.
        '''
        return self.data['blockSize']

