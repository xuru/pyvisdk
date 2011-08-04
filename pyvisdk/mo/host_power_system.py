
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPowerSystem(BaseEntity):
    '''
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostPowerSystem):
        # MUST define these
        super(HostPowerSystem, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def capability(self):
        '''Power system capabilities object.
        '''
        return self.update('capability')

    @property
    def info(self):
        '''Power system state info object.
        '''
        return self.update('info')

