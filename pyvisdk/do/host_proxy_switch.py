
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostProxySwitch(DynamicData):
    '''The HostProxySwitch is a software entity which represents the component of a
        DistributedVirtualSwitch on a particular host.
    '''
    
    def __init__(self, dvsName, dvsUuid, key, mtu, numPorts, numPortsAvailable, pnic, spec, uplinkPort):
        # MUST define these
        super(HostProxySwitch, self).__init__()
    
        self.data['dvsName'] = dvsName
        self.data['dvsUuid'] = dvsUuid
        self.data['key'] = key
        self.data['mtu'] = mtu
        self.data['numPorts'] = numPorts
        self.data['numPortsAvailable'] = numPortsAvailable
        self.data['pnic'] = pnic
        self.data['spec'] = spec
        self.data['uplinkPort'] = uplinkPort
    
    
    @property
    def dvsName(self):
        '''The name of the DistributedVirtualSwitch that the HostProxySwitch is part of.
        '''
        return self.data['dvsName']

    @property
    def dvsUuid(self):
        '''The uuid of the DistributedVirtualSwitch that the HostProxySwitch is a part of.
        '''
        return self.data['dvsUuid']

    @property
    def key(self):
        '''The proxy switch key.
        '''
        return self.data['key']

    @property
    def mtu(self):
        '''The maximum transmission unit (MTU) associated with this switch in bytes.
        '''
        return self.data['mtu']

    @property
    def numPorts(self):
        '''The number of ports that this switch currently has.
        '''
        return self.data['numPorts']

    @property
    def numPortsAvailable(self):
        '''The number of ports that are available on this virtual switch.
        '''
        return self.data['numPortsAvailable']

    @property
    def pnic(self):
        '''The set of physical network adapters associated with this switch.
        '''
        return self.data['pnic']

    @property
    def spec(self):
        '''The specification of the switch.
        '''
        return self.data['spec']

    @property
    def uplinkPort(self):
        '''The list of ports that can be potentially used by physical nics. This property
        contains the keys and names of such ports.
        '''
        return self.data['uplinkPort']

