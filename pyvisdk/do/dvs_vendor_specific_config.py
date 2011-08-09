
from pyvisdk.do.inheritable_policy import InheritablePolicy
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVSVendorSpecificConfig(InheritablePolicy):
    '''This data object type describes vendor specific configuration.
    '''
    
    def __init__(self, keyValue):
        # MUST define these
        super(DVSVendorSpecificConfig, self).__init__()
    
        self.data['keyValue'] = keyValue
    
    
    @property
    def keyValue(self):
        '''An opaque binary blob that stores vendor specific configuration.
        '''
        return self.data['keyValue']

