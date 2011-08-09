
from pyvisdk.do.license_source import LicenseSource
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LocalLicenseSource(LicenseSource):
    '''Specify license key data to store locally.
    '''
    
    def __init__(self, licenseKeys):
        # MUST define these
        super(LocalLicenseSource, self).__init__()
    
        self.data['licenseKeys'] = licenseKeys
    
    
    @property
    def licenseKeys(self):
        '''The size of this string is implementation dependent. It must contain ASCII or ISO
        Latin-1 characters only.
        '''
        return self.data['licenseKeys']

