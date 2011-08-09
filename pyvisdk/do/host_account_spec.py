
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostAccountSpec(DynamicData):
    '''This data object type contains common parameters for local account creation. The
        password and description properties are not supported for group accounts
        on POSIX hosts.
    '''
    
    def __init__(self, description, id, password):
        # MUST define these
        super(HostAccountSpec, self).__init__()
    
        self.data['description'] = description
        self.data['id'] = id
        self.data['password'] = password
    
    
    @property
    def description(self):
        '''The description of the specified account.
        '''
        return self.data['description']

    @property
    def id(self):
        '''The ID of the specified account.
        '''
        return self.data['id']

    @property
    def password(self):
        '''The password for a user or group.
        '''
        return self.data['password']

