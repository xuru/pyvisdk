
from pyvisdk.do.host_directory_store_info import HostDirectoryStoreInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostActiveDirectoryInfo(HostDirectoryStoreInfo):
    '''The HostActiveDirectoryInfo data object describes ESX host membership in an Active
        Directory domain. If the HostAuthenticationStoreInfo.enabled property is ,
        the host is a member of a domain and the ESX Server will set the domain
        information properties.
    '''
    
    def __init__(self, domainMembershipStatus, joinedDomain, trustedDomain):
        # MUST define these
        super(HostActiveDirectoryInfo, self).__init__()
    
        self.data['domainMembershipStatus'] = domainMembershipStatus
        self.data['joinedDomain'] = joinedDomain
        self.data['trustedDomain'] = trustedDomain
    
    
    @property
    def domainMembershipStatus(self):
        '''Health information about the domain membership. See
        HostActiveDirectoryInfoDomainMembershipStatus.
        '''
        return self.data['domainMembershipStatus']

    @property
    def joinedDomain(self):
        '''The domain that this host joined.
        '''
        return self.data['joinedDomain']

    @property
    def trustedDomain(self):
        '''List of domains with which the
        '''
        return self.data['trustedDomain']

