
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HttpNfcLeaseHostInfo(DynamicData):
    '''Contains information about how to connect to a given host.
    '''
    
    def __init__(self, sslThumbprint, url):
        # MUST define these
        super(HttpNfcLeaseHostInfo, self).__init__()
    
        self.data['sslThumbprint'] = sslThumbprint
        self.data['url'] = url
    
    
    @property
    def sslThumbprint(self):
        '''SSL thumbprint for the host the URL refers to. Empty if no SSL thumbprint is
        available or needed.
        '''
        return self.data['sslThumbprint']

    @property
    def url(self):
        '''The host url will be of the form
        '''
        return self.data['url']

