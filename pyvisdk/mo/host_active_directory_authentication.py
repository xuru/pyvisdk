
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
    
    
    
    
    
    def JoinDomain_Task(self):
        '''Adds the host to an Active Directory domain.If the
        HostAuthenticationStoreInfo.enabled property is True (accessed through the info
        property), the host has joined a domain. The vSphere API will throw the
        InvalidState fault if you try to add a host to a domain when the host has
        already joined a domain.
        :rtype: ManagedObjectReference to a Task
        :returns: 
        '''
        return self.delegate("JoinDomain_Task")()
    
    def LeaveCurrentDomain_Task(self):
        '''Removes the host from the Active Directory domain to which it belongs.
        :rtype: ManagedObjectReference to a Task
        :returns: 
        '''
        return self.delegate("LeaveCurrentDomain_Task")()