
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostAuthenticationManager(BaseEntity):
    '''The vSphere API supports Microsoft Active Directory management of authentication
        for ESX hosts. To integrate an ESX host into an Active Directory
        environment, you use an Active Directory account that has the authority to
        add a computer to a domain. The ESX Server locates the Active Directory
        domain controller. When you add a host to a domain, you only need to
        specify the domain and the account user name and password.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostAuthenticationManager):
        # MUST define these
        super(HostAuthenticationManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def info(self):
        '''Information about Active Directory membership.
        '''
        return self.update('info')

    @property
    def supportedStore(self):
        '''An array that can contain managed object references to local and Active Directory
        authentication managed objects.
        '''
        return self.update('supportedStore')

