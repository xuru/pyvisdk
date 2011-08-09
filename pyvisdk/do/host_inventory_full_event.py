
from pyvisdk.do.license_event import LicenseEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostInventoryFullEvent(LicenseEvent):
    '''This event records if the inventory of hosts has reached capacity.
    '''
    
    def __init__(self, capacity):
        # MUST define these
        super(HostInventoryFullEvent, self).__init__()
    
        self.data['capacity'] = capacity
    
    
    @property
    def capacity(self):
        '''
        '''
        return self.data['capacity']

