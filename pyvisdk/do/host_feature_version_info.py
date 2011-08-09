
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostFeatureVersionInfo(DynamicData):
    '''Feature-specific version information for a host
    '''
    
    def __init__(self, key, value):
        # MUST define these
        super(HostFeatureVersionInfo, self).__init__()
    
        self.data['key'] = key
        self.data['value'] = value
    
    
    @property
    def key(self):
        '''A unique key that identifies a feature, list of possible values are specified in
        HostFeatureVersionKey
        '''
        return self.data['key']

    @property
    def value(self):
        '''The version string of this feature
        '''
        return self.data['value']

