
from pyvisdk.do.apply_profile import ApplyProfile
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class OptionProfile(ApplyProfile):
    '''DataObject that encapsulates one advanced configuration
    '''
    
    def __init__(self, key):
        # MUST define these
        super(OptionProfile, self).__init__()
    
        self.data['key'] = key
    
    
    @property
    def key(self):
        '''The linkable identifier
        '''
        return self.data['key']

