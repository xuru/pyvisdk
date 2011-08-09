
from pyvisdk.do.license_event import LicenseEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LicenseNonComplianceEvent(LicenseEvent):
    '''This event records that the inventory is not license compliant.
    '''
    
    def __init__(self, url):
        # MUST define these
        super(LicenseNonComplianceEvent, self).__init__()
    
        self.data['url'] = url
    
    
    @property
    def url(self):
        '''Gives the url at which more details about non-compliance can be found.
        '''
        return self.data['url']

