
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.host_authentication_store import HostAuthenticationStore

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDirectoryStore(HostAuthenticationStore):
    '''HostDirectoryStore is a base class for directory-based authentication stores.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostDirectoryStore):
        super(HostDirectoryStore, self).__init__(core, name=name, ref=ref, type=type)

    

    