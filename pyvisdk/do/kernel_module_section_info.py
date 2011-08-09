
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class KernelModuleSectionInfo(DynamicData):
    '''Information about a module section.
    '''
    
    def __init__(self, address, length):
        # MUST define these
        super(KernelModuleSectionInfo, self).__init__()
    
        self.data['address'] = address
        self.data['length'] = length
    
    
    @property
    def address(self):
        '''Base address of section.
        '''
        return self.data['address']

    @property
    def length(self):
        '''Section length.
        '''
        return self.data['length']

