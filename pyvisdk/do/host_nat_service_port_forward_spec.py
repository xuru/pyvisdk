
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostNatServicePortForwardSpec(DynamicData):
    '''This data object type describes the Network Address Translation (NAT) port
        forwarding specification.
    '''
    
    def __init__(self, guestIpAddress, guestPort, hostPort, name, type):
        # MUST define these
        super(HostNatServicePortForwardSpec, self).__init__()
    
        self.data['guestIpAddress'] = guestIpAddress
        self.data['guestPort'] = guestPort
        self.data['hostPort'] = hostPort
        self.data['name'] = name
        self.data['type'] = type
    
    
    @property
    def guestIpAddress(self):
        '''The IP address for the guest. Network traffic from the host is forwarded to this
        IP address.
        '''
        return self.data['guestIpAddress']

    @property
    def guestPort(self):
        '''The port number for the guest. Network traffic from the host is forwarded to this
        port.
        '''
        return self.data['guestPort']

    @property
    def hostPort(self):
        '''The port number on the host. Network traffic sent to the host on this TCP/UDP port
        is forwarded to the guest at the specified IP address and port.
        '''
        return self.data['hostPort']

    @property
    def name(self):
        '''The user-defined name to identify the service being forwarded. No white spaces are
        allowed in the string.
        '''
        return self.data['name']

    @property
    def type(self):
        '''Either "tcp" or "udp".
        '''
        return self.data['type']

