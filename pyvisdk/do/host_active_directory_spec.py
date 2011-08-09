
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostActiveDirectorySpec(DynamicData):
    '''The HostActiveDirectorySpec data object defines properties for Active Directory
        domain access.
    '''
    
    def __init__(self, domainName, password, userName):
        # MUST define these
        super(HostActiveDirectorySpec, self).__init__()
    
        self.data['domainName'] = domainName
        self.data['password'] = password
        self.data['userName'] = userName
    
    
    @property
    def domainName(self):
        '''Domain name.
        '''
        return self.data['domainName']

    @property
    def password(self):
        '''Password for the Active Directory account.
        '''
        return self.data['password']

    @property
    def userName(self):
        '''Name of an Active Directory account with the authority to add a host to the
        domain.
        '''
        return self.data['userName']

