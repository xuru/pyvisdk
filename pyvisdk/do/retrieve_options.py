
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class RetrieveOptions(DynamicData):
    '''Options for RetrievePropertiesEx.
    '''
    
    def __init__(self, maxObjects):
        # MUST define these
        super(RetrieveOptions, self).__init__()
    
        self.data['maxObjects'] = maxObjects
    
    
    @property
    def maxObjects(self):
        '''The maximum number of ObjectContent data objects that should be returned in a
        single result from RetrievePropertiesEx.
        '''
        return self.data['maxObjects']

