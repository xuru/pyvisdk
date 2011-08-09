
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ResourceAllocationOption(DynamicData):
    '''The ResourceAllocationOption data object specifies value ranges and default values
        for ResourceAllocationInfo.
    '''
    
    def __init__(self, sharesOption):
        # MUST define these
        super(ResourceAllocationOption, self).__init__()
    
        self.data['sharesOption'] = sharesOption
    
    
    @property
    def sharesOption(self):
        '''Default value and value range for shares.
        '''
        return self.data['sharesOption']

