
from pyvisdk.do.license_event import LicenseEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LicenseRestrictedEvent(LicenseEvent):
    '''This event records if the required licenses could not be reserved because of a
        restriction in the option file.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(LicenseRestrictedEvent, self).__init__()
    

    
    
