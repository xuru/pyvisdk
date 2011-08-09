
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPortGroup(DynamicData):
    '''This data object type is used to describe port groups. Port groups are used to
        group virtual network adapters on a virtual switch, associating them with
        networks and network policies.
    '''
    
    def __init__(self, computedPolicy, key, port, spec, vswitch):
        # MUST define these
        super(HostPortGroup, self).__init__()
    
        self.data['computedPolicy'] = computedPolicy
        self.data['key'] = key
        self.data['port'] = port
        self.data['spec'] = spec
        self.data['vswitch'] = vswitch
    
    
    @property
    def computedPolicy(self):
        '''Computed network policies that are applicable for a port group. The inheritance
        scheme for PortGroup requires knowledge about the NetworkPolicy for a port
        group and its parent virtual switch as well as the logic for computing the
        results. This information is provided as a convenience so that callers
        need not duplicate the inheritance logic to determine the proper values
        for a network policy.
        '''
        return self.data['computedPolicy']

    @property
    def key(self):
        '''The linkable identifier.
        '''
        return self.data['key']

    @property
    def port(self):
        '''The ports that currently exist and are used on this port group.
        '''
        return self.data['port']

    @property
    def spec(self):
        '''The specification of a port group.
        '''
        return self.data['spec']

    @property
    def vswitch(self):
        '''The virtual switch that contains this port group.
        '''
        return self.data['vswitch']

