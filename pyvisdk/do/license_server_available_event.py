
from pyvisdk.do.license_event import LicenseEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LicenseServerAvailableEvent(LicenseEvent):
    '''This event is reported if the LicenseServer was previously unreachable and is now
        reachable.
    '''
    
    def __init__(self, licenseServer):
        # MUST define these
        super(LicenseServerAvailableEvent, self).__init__()
    
        self.data['licenseServer'] = licenseServer
    
    
    @property
    def licenseServer(self):
        '''
        '''
        return self.data['licenseServer']

