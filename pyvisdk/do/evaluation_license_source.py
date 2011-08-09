
from pyvisdk.do.license_source import LicenseSource
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class EvaluationLicenseSource(LicenseSource):
    '''Specify an evaluation license source. Feature licensing is not required while the
        remaining hours is greater than zero.
    '''
    
    def __init__(self, remainingHours):
        # MUST define these
        super(EvaluationLicenseSource, self).__init__()
    
        self.data['remainingHours'] = remainingHours
    
    
    @property
    def remainingHours(self):
        '''The number of remaining hours before product evaluation expires
        '''
        return self.data['remainingHours']

