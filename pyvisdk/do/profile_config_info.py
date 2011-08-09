
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfileConfigInfo(DynamicData):
    '''
    '''
    
    def __init__(self, annotation, enabled, name):
        # MUST define these
        super(ProfileConfigInfo, self).__init__()
    
        self.data['annotation'] = annotation
        self.data['enabled'] = enabled
        self.data['name'] = name
    
    
    @property
    def annotation(self):
        '''User Provided description of the profile
        '''
        return self.data['annotation']

    @property
    def enabled(self):
        '''Flag indicating if the Profile is enabled
        '''
        return self.data['enabled']

    @property
    def name(self):
        '''Name of the profile
        '''
        return self.data['name']

