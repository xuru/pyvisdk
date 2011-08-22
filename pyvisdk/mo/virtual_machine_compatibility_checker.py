
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineCompatibilityChecker(BaseEntity):
    '''A singleton managed object that can answer questions about compatibility of a
    virtual machine with a host.'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.VirtualMachineCompatibilityChecker):
        super(VirtualMachineCompatibilityChecker, self).__init__(core, name=name, ref=ref, type=type)
    
    
    
    