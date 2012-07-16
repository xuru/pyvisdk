
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.host_authentication_store import HostAuthenticationStore

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostLocalAuthentication(HostAuthenticationStore):
    '''The HostLocalAuthentication managed object represents local authentication for
    user accounts on an ESX host.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostLocalAuthentication):
        super(HostLocalAuthentication, self).__init__(core, name=name, ref=ref, type=type)

    

    