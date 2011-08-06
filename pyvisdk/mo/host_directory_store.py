
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.host_authentication_store import HostAuthenticationStore
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDirectoryStore(HostAuthenticationStore):
    '''Properties
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostDirectoryStore):
        # MUST define these
        super(HostDirectoryStore, self).__init__(core, name=name, ref=ref, type=type)
    
    
