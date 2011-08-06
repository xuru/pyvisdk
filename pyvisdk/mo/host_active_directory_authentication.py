
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.host_directory_store import HostDirectoryStore
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostActiveDirectoryAuthentication(HostDirectoryStore):
    '''Properties
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostActiveDirectoryAuthentication):
        # MUST define these
        super(HostActiveDirectoryAuthentication, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def JoinDomain_Task(self, domainName, userName, password):
        '''Adds the host to an Active Directory domain.If the
        HostAuthenticationStoreInfo.enabled property is True (accessed through the
        info property), the host has joined a domain. The vSphere API will throw
        the InvalidState fault if you try to add a host to a domain when the host
        has already joined a domain.

        :param domainName: Name of the domain to be joined.

        :param userName: Name for an Active Directory account that has the authority to add hosts to the
        domain.

        :param password: Password for theaccount.


        :rtype: Task 

        '''
        
        return self.delegate("JoinDomain_Task")(domainName,userName,password)
        

    def LeaveCurrentDomain_Task(self, force):
        '''Removes the host from the Active Directory domain to which it belongs.

        :param force: If, any existing permissions on managed entities for Active Directory users will
        be deleted. Ifand such permissions exist, the operation will fail.


        :rtype: Task 

        '''
        
        return self.delegate("LeaveCurrentDomain_Task")(force)
        
