
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostVirtualNic(DynamicData):
    '''This data object type describes a virtual network adapter representing an adapter
        that connects to a virtual switch. A VirtualNic differs from a PhysicalNic
        in that the latter corresponds to a physical device that is connected to
        the physical network. The former is a virtual device that is connected to
        a virtual switch. A VirtualNic accesses the external network through a
        virtual switch that is bridged through a PhysicalNic to a physical
        network.
    '''
    
    def __init__(self, device, key, port, portgroup, spec):
        # MUST define these
        super(HostVirtualNic, self).__init__()
    
        self.data['device'] = device
        self.data['key'] = key
        self.data['port'] = port
        self.data['portgroup'] = portgroup
        self.data['spec'] = spec
    
    
    @property
    def device(self):
        '''Device name.
        '''
        return self.data['device']

    @property
    def key(self):
        '''The linkable identifier.
        '''
        return self.data['key']

    @property
    def port(self):
        '''The port on the port group that the virtual network adapter is using when it is
        enabled.
        '''
        return self.data['port']

    @property
    def portgroup(self):
        '''If the vnic is connecting to a vSwitch, this property is the name of portgroup
        connected. If the vnic is connecting to a DistributedVirtualSwitch, this
        property is an empty string.
        '''
        return self.data['portgroup']

    @property
    def spec(self):
        '''The configurable properties for the virtual network adapter object.
        '''
        return self.data['spec']

