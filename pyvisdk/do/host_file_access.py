
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostFileAccess(DynamicData):
    '''This data object type contains a single access control entry for a file
        permissions list.
    '''
    
    def __init__(self, what, who):
        # MUST define these
        super(HostFileAccess, self).__init__()
    
        self.data['what'] = what
        self.data['who'] = who
    
    
    @property
    def what(self):
        '''Rights given to the user or group.
        '''
        return self.data['what']

    @property
    def who(self):
        '''User or group to which the access applies.
        '''
        return self.data['who']

