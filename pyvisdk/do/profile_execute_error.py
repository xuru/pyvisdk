
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfileExecuteError(DynamicData):
    '''DataObject which points to an error encountered during execute.
    '''
    
    def __init__(self, message, path):
        # MUST define these
        super(ProfileExecuteError, self).__init__()
    
        self.data['message'] = message
        self.data['path'] = path
    
    
    @property
    def message(self):
        '''Message describing the error
        '''
        return self.data['message']

    @property
    def path(self):
        '''Path where the error occurred
        '''
        return self.data['path']

