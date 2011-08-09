
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostNatServiceNameServiceSpec(DynamicData):
    '''This data object type specifies the information for the name servers.
    '''
    
    def __init__(self, dnsAutoDetect, dnsNameServer, dnsPolicy, dnsRetries, dnsTimeout, nbdsTimeout, nbnsRetries, nbnsTimeout):
        # MUST define these
        super(HostNatServiceNameServiceSpec, self).__init__()
    
        self.data['dnsAutoDetect'] = dnsAutoDetect
        self.data['dnsNameServer'] = dnsNameServer
        self.data['dnsPolicy'] = dnsPolicy
        self.data['dnsRetries'] = dnsRetries
        self.data['dnsTimeout'] = dnsTimeout
        self.data['nbdsTimeout'] = nbdsTimeout
        self.data['nbnsRetries'] = nbnsRetries
        self.data['nbnsTimeout'] = nbnsTimeout
    
    
    @property
    def dnsAutoDetect(self):
        '''The flag to indicate whether or not the DNS server should be automatically
        detected or specified explicitly.
        '''
        return self.data['dnsAutoDetect']

    @property
    def dnsNameServer(self):
        '''The list of DNS servers.
        '''
        return self.data['dnsNameServer']

    @property
    def dnsPolicy(self):
        '''The policy to use when multiple DNS addresses are available on the host.
        '''
        return self.data['dnsPolicy']

    @property
    def dnsRetries(self):
        '''The number of retries before giving up on a DNS request from a virtual network.
        '''
        return self.data['dnsRetries']

    @property
    def dnsTimeout(self):
        '''The time (in seconds) before retrying a DNS request to an external network.
        '''
        return self.data['dnsTimeout']

    @property
    def nbdsTimeout(self):
        '''The time (in seconds) allotted for queries to the NetBIOS Datagram Server (NBDS).
        '''
        return self.data['nbdsTimeout']

    @property
    def nbnsRetries(self):
        '''Number of retries for each query to the NBNS.
        '''
        return self.data['nbnsRetries']

    @property
    def nbnsTimeout(self):
        '''The time (in seconds) allotted for queries to the NBNS.
        '''
        return self.data['nbnsTimeout']

