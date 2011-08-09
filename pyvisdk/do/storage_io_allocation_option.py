
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class StorageIOAllocationOption(DynamicData):
    '''The IOAllocationOption specifies value ranges that can be used to initialize
        IOAllocationInfo object.
    '''
    
    def __init__(self, limitOption, sharesOption):
        # MUST define these
        super(StorageIOAllocationOption, self).__init__()
    
        self.data['limitOption'] = limitOption
        self.data['sharesOption'] = sharesOption
    
    
    @property
    def limitOption(self):
        '''limitOptions defines a range of values allowed to be used for storage IO limit
        limit.
        '''
        return self.data['limitOption']

    @property
    def sharesOption(self):
        '''sharesOption defines a range of values allowed to be used to specify allocated io
        shares shares.
        '''
        return self.data['sharesOption']

