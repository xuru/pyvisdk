
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostAuthenticationManagerInfo(DynamicData):
    '''The HostAuthenticationManagerInfo data object provides access to authentication
        information for the ESX host.
    '''
    
    def __init__(self, authConfig):
        # MUST define these
        super(HostAuthenticationManagerInfo, self).__init__()
    
        self.data['authConfig'] = authConfig
    
    
    @property
    def authConfig(self):
        '''An array containing entries for local authentication and host Active Directory
        authentication. * HostLocalAuthenticationInfo - Local authentication is
        always enabled. * HostActiveDirectoryInfo - Host Active Directory
        authentication information includes the name of the domain, membership
        status, and a list of other domains trusted by the membership domain.
        '''
        return self.data['authConfig']

