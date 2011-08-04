
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.host_authentication_store import HostAuthenticationStore
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostLocalAuthentication(HostAuthenticationStore):
    '''Methods
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostLocalAuthentication):
        # MUST define these
        super(HostLocalAuthentication, self).__init__(core, name=name, ref=ref, type=type)
    
    
