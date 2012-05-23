
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostAuthenticationStore(BaseEntity):
    '''The HostAuthenticationStore base class represents both local user and host
    Active Directory authentication for an ESX host.* Local user authentication is
    always enabled. The vSphere API does not support local user configuration for a
    host. * Active Directory authentication for ESX hosts relies on an established
    Active Directory account that has the authority to add the host to a domain.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostAuthenticationStore):
        super(HostAuthenticationStore, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def info(self):
        '''Information about the authentication store.'''
        return self.update('info')

    