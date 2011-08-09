
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostSslThumbprintInfo(DynamicData):
    '''The SSL thumbprint information for a host to login into other hosts in the same
        cluster without username/password authentication.
    '''
    
    def __init__(self, principal, sslThumbprints):
        # MUST define these
        super(HostSslThumbprintInfo, self).__init__()
    
        self.data['principal'] = principal
        self.data['sslThumbprints'] = sslThumbprints
    
    
    @property
    def principal(self):
        '''The principal used for the login session
        '''
        return self.data['principal']

    @property
    def sslThumbprints(self):
        '''SSL thumbprints of other hosts in the same cluster
        '''
        return self.data['sslThumbprints']

