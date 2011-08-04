
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostAuthenticationStore(BaseEntity):
    '''Properties
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostAuthenticationStore):
        # MUST define these
        super(HostAuthenticationStore, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def info(self):
        '''Information about the authentication store.
        '''
        return self.update('info')

