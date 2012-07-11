
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualizationManager(BaseEntity):
    '''The VirtualizationManager is the interface for discover and consolidate host
    and services from physical environment to virtualization environment.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.VirtualizationManager):
        super(VirtualizationManager, self).__init__(core, name=name, ref=ref, type=type)

    

    