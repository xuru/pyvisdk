
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class SessionManagerLocalTicket(DynamicData):
    '''This data object type contains the user name and location of the file containing
        the password that clients can use for one-time logon to a server.
    '''
    
    def __init__(self, passwordFilePath, userName):
        # MUST define these
        super(SessionManagerLocalTicket, self).__init__()
    
        self.data['passwordFilePath'] = passwordFilePath
        self.data['userName'] = userName
    
    
    @property
    def passwordFilePath(self):
        '''Absolute local path to the file containing a one-time password.
        '''
        return self.data['passwordFilePath']

    @property
    def userName(self):
        '''User name to be used for logon.
        '''
        return self.data['userName']

