
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.managed_entity import ManagedEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ComputeResource(ManagedEntity):
    '''Represents a set of physical compute resources for a set of virtual machines.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.ComputeResource):
        # MUST define these
        super(ComputeResource, self).__init__(core, name=name, ref=ref, type=type)
    
    
