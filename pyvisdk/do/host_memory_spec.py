
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostMemorySpec(DynamicData):
    '''DataObject used for configuring the memory setting
    '''
    
    def __init__(self, serviceConsoleReservation):
        # MUST define these
        super(HostMemorySpec, self).__init__()
    
        self.data['serviceConsoleReservation'] = serviceConsoleReservation
    
    
    @property
    def serviceConsoleReservation(self):
        '''Service Console reservation in bytes.
        '''
        return self.data['serviceConsoleReservation']

