
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.managed_entity import ManagedEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class Network(ManagedEntity):
    '''Represents a network accessible by either hosts or virtual machines. This can
    be a physical network or a logical network, such as a VLAN.Networks are
    created:* explicitly when configuring a host. * automatically when adding a
    host to VirtualCenter. * automatically when adding a new virtual machine to a
    host or to VirtualCenter.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.Network):
        super(Network, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def host(self):
        '''Hosts attached to this network.'''
        return self.update('host')
    @property
    def name(self):
        '''Name of this network.'''
        return self.update('name')
    @property
    def summary(self):
        '''Properties of a network.'''
        return self.update('summary')
    @property
    def vm(self):
        '''Virtual machines using this network.'''
        return self.update('vm')

    
    
    def DestroyNetwork(self):
        '''<b>Deprecated.</b> <i>As of VI API 2.5 do not use this method. This method
        throws ResourceInUse. Networks are automatically removed when no longer in use,
        so this method is unnecessary.</i> Removes a network. A network can be removed
        only if it is not used by any host or virtual machine.
        
        '''
        return self.delegate("DestroyNetwork")()