
from pyvisdk.do.apply_profile import ApplyProfile
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PnicUplinkProfile(ApplyProfile):
    '''DataObject which specifies the mapping between a PNic and an uplink port
    '''
    
    def __init__(self, key):
        # MUST define these
        super(PnicUplinkProfile, self).__init__()
    
        self.data['key'] = key
    
    
    @property
    def key(self):
        '''The linkable identifier
        '''
        return self.data['key']

