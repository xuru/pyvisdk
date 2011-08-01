
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPowerSystem(BaseEntity):
    '''Managed object responsible for getting and setting host power management policies.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostPowerSystem):
        # MUST define these
        super(HostPowerSystem, self).__init__(core, name=name, ref=ref, type=type)
    
    
