
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostAuthenticationStore(BaseEntity):
    '''The HostAuthenticationStore base class represents both local user and host Active
        Directory authentication for an ESX host.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostAuthenticationStore):
        # MUST define these
        super(HostAuthenticationStore, self).__init__(core, name=name, ref=ref, type=type)
    
    
