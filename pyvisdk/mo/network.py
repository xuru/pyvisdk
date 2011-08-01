
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.managed_entity import ManagedEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class Network(ManagedEntity):
    '''Represents a network accessible by either hosts or virtual machines. This can be a
        physical network or a logical network, such as a VLAN.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.Network):
        # MUST define these
        super(Network, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def name(self):
        '''
        Name of this network.
        '''
        return self.update('name')

