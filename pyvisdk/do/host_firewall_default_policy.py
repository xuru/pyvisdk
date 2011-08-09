
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostFirewallDefaultPolicy(DynamicData):
    '''Default settings for the firewall, used for ports that are not explicitly opened.
    '''
    
    def __init__(self, incomingBlocked, outgoingBlocked):
        # MUST define these
        super(HostFirewallDefaultPolicy, self).__init__()
    
        self.data['incomingBlocked'] = incomingBlocked
        self.data['outgoingBlocked'] = outgoingBlocked
    
    
    @property
    def incomingBlocked(self):
        '''Flag indicating whether incoming traffic should be blocked by default.
        '''
        return self.data['incomingBlocked']

    @property
    def outgoingBlocked(self):
        '''Flag indicating whether outgoing traffic should be blocked by default.
        '''
        return self.data['outgoingBlocked']

