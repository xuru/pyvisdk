
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LicenseUsageInfo(DynamicData):
    '''Contains source information, licensed features, and usage.
    '''
    
    def __init__(self, featureInfo, reservationInfo, source, sourceAvailable):
        # MUST define these
        super(LicenseUsageInfo, self).__init__()
    
        self.data['featureInfo'] = featureInfo
        self.data['reservationInfo'] = reservationInfo
        self.data['source'] = source
        self.data['sourceAvailable'] = sourceAvailable
    
    
    @property
    def featureInfo(self):
        '''Includes all the features that are referenced in the reservation array.
        '''
        return self.data['featureInfo']

    @property
    def reservationInfo(self):
        '''A list of feature reservations.
        '''
        return self.data['reservationInfo']

    @property
    def source(self):
        '''The source from which licensing data is acquired.
        '''
        return self.data['source']

    @property
    def sourceAvailable(self):
        '''Returns whether or not the source is currently available.
        '''
        return self.data['sourceAvailable']

