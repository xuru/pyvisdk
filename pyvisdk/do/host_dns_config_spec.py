
from pyvisdk.do.host_dns_config import HostDnsConfig
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDnsConfigSpec(HostDnsConfig):
    '''Dataobject for configuring the DNS settings on the host.
    '''
    
    def __init__(self, virtualNicConnection):
        # MUST define these
        super(HostDnsConfigSpec, self).__init__()
    
        self.data['virtualNicConnection'] = virtualNicConnection
    
    
    @property
    def virtualNicConnection(self):
        '''Choose a Virtual nic based on what it is connected to.
        '''
        return self.data['virtualNicConnection']

