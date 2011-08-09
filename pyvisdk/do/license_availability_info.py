
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LicenseAvailabilityInfo(DynamicData):
    '''Describes how many licenses of a particular feature is provided by the licensing
        source.
    '''
    
    def __init__(self, available, feature, total):
        # MUST define these
        super(LicenseAvailabilityInfo, self).__init__()
    
        self.data['available'] = available
        self.data['feature'] = feature
        self.data['total'] = total
    
    
    @property
    def available(self):
        '''The number of licenses that have not yet been reserved on the source.
        '''
        return self.data['available']

    @property
    def feature(self):
        '''Describes the feature.
        '''
        return self.data['feature']

    @property
    def total(self):
        '''Total number of licenses for this given type that are installed on the source.
        '''
        return self.data['total']

