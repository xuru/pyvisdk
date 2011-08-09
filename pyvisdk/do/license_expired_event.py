
from pyvisdk.do.event import Event
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LicenseExpiredEvent(Event):
    '''This event records the expiration of a license.
    '''
    
    def __init__(self, feature):
        # MUST define these
        super(LicenseExpiredEvent, self).__init__()
    
        self.data['feature'] = feature
    
    
    @property
    def feature(self):
        '''
        '''
        return self.data['feature']

