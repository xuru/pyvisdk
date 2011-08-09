
from pyvisdk.do.inheritable_policy import InheritablePolicy
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVSSecurityPolicy(InheritablePolicy):
    '''This data object type describes security policy governing ports.
    '''
    
    def __init__(self, allowPromiscuous, forgedTransmits, macChanges):
        # MUST define these
        super(DVSSecurityPolicy, self).__init__()
    
        self.data['allowPromiscuous'] = allowPromiscuous
        self.data['forgedTransmits'] = forgedTransmits
        self.data['macChanges'] = macChanges
    
    
    @property
    def allowPromiscuous(self):
        '''The flag to indicate whether or not all traffic is seen on the port.
        '''
        return self.data['allowPromiscuous']

    @property
    def forgedTransmits(self):
        '''The flag to indicate whether or not the virtual network adapter should be allowed
        to send network traffic with a different MAC address than that of the
        virtual network adapter.
        '''
        return self.data['forgedTransmits']

    @property
    def macChanges(self):
        '''The flag to indicate whether or not the Media Access Control (MAC) address can be
        changed.
        '''
        return self.data['macChanges']

