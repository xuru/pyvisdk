
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostVirtualSwitch(DynamicData):
    '''The virtual switch is a software entity to which multiple virtual network adapters
        can connect to create a virtual network. It can also be bridged to a
        physical network.
    '''
    
    def __init__(self, key, mtu, name, numPorts, numPortsAvailable, pnic, portgroup, spec):
        # MUST define these
        super(HostVirtualSwitch, self).__init__()
    
        self.data['key'] = key
        self.data['mtu'] = mtu
        self.data['name'] = name
        self.data['numPorts'] = numPorts
        self.data['numPortsAvailable'] = numPortsAvailable
        self.data['pnic'] = pnic
        self.data['portgroup'] = portgroup
        self.data['spec'] = spec
    
    
    @property
    def key(self):
        '''The virtual switch key.
        '''
        return self.data['key']

    @property
    def mtu(self):
        '''The maximum transmission unit (MTU) associated with this virtual switch in bytes.
        '''
        return self.data['mtu']

    @property
    def name(self):
        '''The name of the virtual switch. Maximum length is 32 characters.
        '''
        return self.data['name']

    @property
    def numPorts(self):
        '''The number of ports that this virtual switch currently has.
        '''
        return self.data['numPorts']

    @property
    def numPortsAvailable(self):
        '''The number of ports that are available on this virtual switch. There are a number
        of networking services that utilize a port on the virtual switch and are
        not accounted for in the Port array of a PortGroup. For example, each
        physical NIC attached to a virtual switch consumes one port. This property
        should be used when attempting to implement admission control for new
        services attaching to virtual switches.
        '''
        return self.data['numPortsAvailable']

    @property
    def pnic(self):
        '''The set of physical network adapters associated with this bridge.
        '''
        return self.data['pnic']

    @property
    def portgroup(self):
        '''The list of port groups configured for this virtual switch.
        '''
        return self.data['portgroup']

    @property
    def spec(self):
        '''The specification of a PortGroup.
        '''
        return self.data['spec']

