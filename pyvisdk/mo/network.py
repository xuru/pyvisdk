
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.managed_entity import ManagedEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class Network(ManagedEntity):
    '''Represents a network accessible by either hosts or virtual machines. This can be a
        physical network or a logical network, such as a VLAN.Networks are
        created:
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.Network):
        # MUST define these
        super(Network, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def host(self):
        '''Hosts attached to this network.
        '''
        return self.update('host')

    @property
    def summary(self):
        '''Properties of a network.
        '''
        return self.update('summary')

    @property
    def vm(self):
        '''Virtual machines using this network.
        '''
        return self.update('vm')

