
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostAuthenticationStoreInfo(DynamicData):
    '''The HostAuthenticationStoreInfo base class defines status information for local
        and host Active Directory authentication.
    '''
    
    def __init__(self, enabled):
        # MUST define these
        super(HostAuthenticationStoreInfo, self).__init__()
    
        self.data['enabled'] = enabled
    
    
    @property
    def enabled(self):
        '''Indicates whether the authentication store is configured. * Host Active Directory
        authentication -
        '''
        return self.data['enabled']

