
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class NetIpStackInfoDefaultRouter(DynamicData):
    '''
    '''
    
    def __init__(self, device, ipAddress, lifetime, preference):
        # MUST define these
        super(NetIpStackInfoDefaultRouter, self).__init__()
    
        self.data['device'] = device
        self.data['ipAddress'] = ipAddress
        self.data['lifetime'] = lifetime
        self.data['preference'] = preference
    
    
    @property
    def device(self):
        '''This value will contain the name of the interface as reported by the operationg
        system.
        '''
        return self.data['device']

    @property
    def ipAddress(self):
        '''Unicast IP address of a next-hop router.
        '''
        return self.data['ipAddress']

    @property
    def lifetime(self):
        '''When this entry will no longer valid. For IPv6 this value see For IPv6 RFC 2462
        sections 4.2 and 6.3.4.
        '''
        return self.data['lifetime']

    @property
    def preference(self):
        '''Value of this entry compared to others that this IP stack uses when making
        selection to route traffic on the default route when there are multiple
        default routers. Value must be one of NetIpStackInfoPreference
        '''
        return self.data['preference']

