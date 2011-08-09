
from pyvisdk.do.license_event import LicenseEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ServerLicenseExpiredEvent(LicenseEvent):
    '''This event records an expired VirtualCenter server license.
    '''
    
    def __init__(self, product):
        # MUST define these
        super(ServerLicenseExpiredEvent, self).__init__()
    
        self.data['product'] = product
    
    
    @property
    def product(self):
        '''
        '''
        return self.data['product']

