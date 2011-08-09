
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostFirewallRule(DynamicData):
    '''This data object type describes a port (or range of ports), identified by port
        number(s), direction and protocol. It is used as a convenient way for
        users to express what ports they want to permit through the firewall.
    '''
    
    def __init__(self, direction, endPort, port, protocol):
        # MUST define these
        super(HostFirewallRule, self).__init__()
    
        self.data['direction'] = direction
        self.data['endPort'] = endPort
        self.data['port'] = port
        self.data['protocol'] = protocol
    
    
    @property
    def direction(self):
        '''The port direction.
        '''
        return self.data['direction']

    @property
    def endPort(self):
        '''For a port range, the ending port number.
        '''
        return self.data['endPort']

    @property
    def port(self):
        '''The port number.
        '''
        return self.data['port']

    @property
    def protocol(self):
        '''The port protocol. Valid values are defined by the HostFirewallRuleProtocol
        enumeration.
        '''
        return self.data['protocol']

