
from pyvisdk.do.host_account_spec import HostAccountSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPosixAccountSpec(HostAccountSpec):
    '''This data object type contains a POSIX-specific parameter for local account
        creation.
    '''
    
    def __init__(self, posixId, shellAccess):
        # MUST define these
        super(HostPosixAccountSpec, self).__init__()
    
        self.data['posixId'] = posixId
        self.data['shellAccess'] = shellAccess
    
    
    @property
    def posixId(self):
        '''The user ID or group ID of a specified account.
        '''
        return self.data['posixId']

    @property
    def shellAccess(self):
        '''Grants shell access if true. By default, shell access is disallowed. As of vSphere
        API 4.1, this property has effect only on users with Administrator role on
        one or more VIM objects. For all others the default is applied.
        '''
        return self.data['shellAccess']

