
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ExtensionTaskTypeInfo(DynamicData):
    '''This data object type describes task types defined by the extension.
    '''
    
    def __init__(self, taskID):
        # MUST define these
        super(ExtensionTaskTypeInfo, self).__init__()
    
        self.data['taskID'] = taskID
    
    
    @property
    def taskID(self):
        '''The ID of the task type. Should follow java package naming conventions for
        uniqueness.
        '''
        return self.data['taskID']

