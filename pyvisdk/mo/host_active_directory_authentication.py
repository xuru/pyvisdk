
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.host_directory_store import HostDirectoryStore

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostActiveDirectoryAuthentication(HostDirectoryStore):
    '''The HostActiveDirectoryAuthentication managed object indicates domain
    membership status and provides methods for adding a host to and removing a host
    from a domain.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostActiveDirectoryAuthentication):
        super(HostActiveDirectoryAuthentication, self).__init__(core, name=name, ref=ref, type=type)

    

    
    
    def ImportCertificateForCAM_Task(self, certPath, camServer):
        '''Import the CAM server's certificate to the local store of vmwauth.Import the
        CAM server's certificate to the local store of vmwauth.
        
        :param certPath: full path of the certificate on ESXi
        
        :param camServer: IP of server providing the CAM service.
        
        '''
        return self.delegate("ImportCertificateForCAM_Task")(certPath, camServer)
    
    def JoinDomain_Task(self, domainName, userName, password):
        '''Adds the host to an Active Directory domain.Adds the host to an Active
        Directory domain.
        
        :param domainName: Name of the domain to be joined.
        
        :param userName: Name for an Active Directory account that has the authority to add hosts to the domain.
        
        :param password: Password for theaccount.
        
        '''
        return self.delegate("JoinDomain_Task")(domainName, userName, password)
    
    def JoinDomainWithCAM_Task(self, domainName, camServer):
        '''Adds the host to an Active Directory domain through CAM service.Adds the host
        to an Active Directory domain through CAM service.
        
        :param domainName: Name of the domain to be joined.
        
        :param camServer: Name of server providing the CAM service.
        
        '''
        return self.delegate("JoinDomainWithCAM_Task")(domainName, camServer)
    
    def LeaveCurrentDomain_Task(self, force):
        '''Removes the host from the Active Directory domain to which it belongs.
        
        :param force: If, any existing permissions on managed entities for Active Directory users will be deleted. Ifand such permissions exist, the operation will fail.
        
        '''
        return self.delegate("LeaveCurrentDomain_Task")(force)