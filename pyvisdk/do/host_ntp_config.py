
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostNtpConfig(DynamicData):
    '''Configuration information for the NTP (Network Time Protocol) service.
    '''
    
    def __init__(self, server):
        # MUST define these
        super(HostNtpConfig, self).__init__()
    
        self.data['server'] = server
    
    
    @property
    def server(self):
        '''List of time servers, specified as either IP addresses or fully qualified domain
        names (FQDNs).
        '''
        return self.data['server']

