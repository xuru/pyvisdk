
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostLicenseSpec(DynamicData):
    '''
    '''
    
    def __init__(self, disabledFeatureKey, editionKey, enabledFeatureKey, source):
        # MUST define these
        super(HostLicenseSpec, self).__init__()
    
        self.data['disabledFeatureKey'] = disabledFeatureKey
        self.data['editionKey'] = editionKey
        self.data['enabledFeatureKey'] = enabledFeatureKey
        self.data['source'] = source
    
    
    @property
    def disabledFeatureKey(self):
        '''Disabled features. When an edition is set, all the features in it are enabled by
        default. The following parameter gives a finer control on which features
        are disabled.
        '''
        return self.data['disabledFeatureKey']

    @property
    def editionKey(self):
        '''License edition to use
        '''
        return self.data['editionKey']

    @property
    def enabledFeatureKey(self):
        '''Enabled features
        '''
        return self.data['enabledFeatureKey']

    @property
    def source(self):
        '''License source to be used
        '''
        return self.data['source']

