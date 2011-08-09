
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LicenseReservationInfo(DynamicData):
    '''A reservation describes how many licenses of a particular feature are being used
        by a particular feature.
    '''
    
    def __init__(self, key, required, state):
        # MUST define these
        super(LicenseReservationInfo, self).__init__()
    
        self.data['key'] = key
        self.data['required'] = required
        self.data['state'] = state
    
    
    @property
    def key(self):
        '''Key of the License Feature.
        '''
        return self.data['key']

    @property
    def required(self):
        '''Contains the required number of licenses of the particular type that the product
        needs in its current configuration.
        '''
        return self.data['required']

    @property
    def state(self):
        '''Describes the reservation state of a license.
        '''
        return self.data['state']

