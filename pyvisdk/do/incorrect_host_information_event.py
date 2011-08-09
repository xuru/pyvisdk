
from pyvisdk.do.license_event import LicenseEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class IncorrectHostInformationEvent(LicenseEvent):
    '''This event records if the host did not provide the information needed to acquire
        the correct set of licenses.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(IncorrectHostInformationEvent, self).__init__()
    

    
    
