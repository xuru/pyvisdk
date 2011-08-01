
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostAuthenticationManager(BaseEntity):
    '''The HostAuthenticationManager managed object provides access to Active Directory
        configuration information for an ESX host. It also provides access to
        methods for adding a host to or removing a host from an Active Directory
        domain.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostAuthenticationManager):
        # MUST define these
        super(HostAuthenticationManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
