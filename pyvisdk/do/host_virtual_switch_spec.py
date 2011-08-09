
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostVirtualSwitchSpec(DynamicData):
    '''This data object type describes the VirtualSwitch specification representing the
        properties on a VirtualSwitch that can be configured once the object
        exists.
    '''
    
    def __init__(self, bridge, mtu, numPorts, policy):
        # MUST define these
        super(HostVirtualSwitchSpec, self).__init__()
    
        self.data['bridge'] = bridge
        self.data['mtu'] = mtu
        self.data['numPorts'] = numPorts
        self.data['policy'] = policy
    
    
    @property
    def bridge(self):
        '''The bridge specification describes how physical network adapters can be bridged to
        a virtual switch.
        '''
        return self.data['bridge']

    @property
    def mtu(self):
        '''The maximum transmission unit (MTU) of the virtual switch in bytes.
        '''
        return self.data['mtu']

    @property
    def numPorts(self):
        '''The number of ports that this virtual switch is configured to use. Changing this
        setting does not take effect until the next reboot. The maximum value is
        1024, although other constraints, such as memory limits, may establish a
        lower effective limit.
        '''
        return self.data['numPorts']

    @property
    def policy(self):
        '''The virtual switch policy specification. This has a lower precedence than
        PortGroup. If the policy property is not set and you are creating a
        virtual switch, then a default policy property setting is used. If the
        policy property is not set and you are updating a virtual switch, then the
        policy will be unchanged.
        '''
        return self.data['policy']

