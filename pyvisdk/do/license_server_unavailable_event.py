
from pyvisdk.do.license_event import LicenseEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LicenseServerUnavailableEvent(LicenseEvent):
    '''This event is reported if the LicenseServer becomes unreachable.
    '''
    
    def __init__(self, licenseServer):
        # MUST define these
        super(LicenseServerUnavailableEvent, self).__init__()
    
        self.data['licenseServer'] = licenseServer
    
    
    @property
    def licenseServer(self):
        '''
        '''
        return self.data['licenseServer']

