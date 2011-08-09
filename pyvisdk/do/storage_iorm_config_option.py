
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class StorageIORMConfigOption(DynamicData):
    '''Configuration setting ranges for IORMConfigSpec object.
    '''
    
    def __init__(self, congestionThresholdOption, enabledOption):
        # MUST define these
        super(StorageIORMConfigOption, self).__init__()
    
        self.data['congestionThresholdOption'] = congestionThresholdOption
        self.data['enabledOption'] = enabledOption
    
    
    @property
    def congestionThresholdOption(self):
        '''congestionThresholdOption defines value range which can be used for
        congestionThreshold
        '''
        return self.data['congestionThresholdOption']

    @property
    def enabledOption(self):
        '''enabledOption provides default state value for enabled
        '''
        return self.data['enabledOption']

