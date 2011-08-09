
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPortGroupSpec(DynamicData):
    '''This data object type describes the PortGroup specification representing the
        properties on a PortGroup that can be configured.
    '''
    
    def __init__(self, name, policy, vlanId, vswitchName):
        # MUST define these
        super(HostPortGroupSpec, self).__init__()
    
        self.data['name'] = name
        self.data['policy'] = policy
        self.data['vlanId'] = vlanId
        self.data['vswitchName'] = vswitchName
    
    
    @property
    def name(self):
        '''The name of the port group.
        '''
        return self.data['name']

    @property
    def policy(self):
        '''Policies on the port group take precedence over the ones specified on the virtual
        switch.
        '''
        return self.data['policy']

    @property
    def vlanId(self):
        '''The VLAN ID for ports using this port group. Possible values: * A value of 0
        specifies that you do not want the port group associated with a VLAN. * A
        value from 1 to 4094 specifies a VLAN ID for the port group. * A value of
        4095 specifies that the port group should use trunk mode, which allows the
        guest operating system to manage its own VLAN tags.
        '''
        return self.data['vlanId']

    @property
    def vswitchName(self):
        '''The identifier of the virtual switch on which this port group is located.
        '''
        return self.data['vswitchName']

