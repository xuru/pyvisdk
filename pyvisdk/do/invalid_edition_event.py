
from pyvisdk.do.license_event import LicenseEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class InvalidEditionEvent(LicenseEvent):
    '''This event records if the edition is set to an invalid value.
    '''
    
    def __init__(self, feature):
        # MUST define these
        super(InvalidEditionEvent, self).__init__()
    
        self.data['feature'] = feature
    
    
    @property
    def feature(self):
        '''
        '''
        return self.data['feature']

