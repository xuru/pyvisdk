
from pyvisdk.do.license_event import LicenseEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class NoLicenseEvent(LicenseEvent):
    '''These are events reported by License Manager.A NoLicenseEvent is reported if the
        required licenses could not be reserved. Each feature that is not fully
        licensed is reported.
    '''
    
    def __init__(self, feature):
        # MUST define these
        super(NoLicenseEvent, self).__init__()
    
        self.data['feature'] = feature
    
    
    @property
    def feature(self):
        '''
        '''
        return self.data['feature']

