
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class StorageIORMConfigSpec(DynamicData):
    '''Configuration settings used for creating or reconfiguring storage I/O resource
        management.All fields are defined as optional. If a field is unset, the
        property is not changed.
    '''
    
    def __init__(self, congestionThreshold, enabled):
        # MUST define these
        super(StorageIORMConfigSpec, self).__init__()
    
        self.data['congestionThreshold'] = congestionThreshold
        self.data['enabled'] = enabled
    
    
    @property
    def congestionThreshold(self):
        '''The latency beyond which the storage array is considered congested.
        '''
        return self.data['congestionThreshold']

    @property
    def enabled(self):
        '''Flag indicating whether or not the service is enabled.
        '''
        return self.data['enabled']

