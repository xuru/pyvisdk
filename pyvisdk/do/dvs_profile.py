
from pyvisdk.do.apply_profile import ApplyProfile
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DvsProfile(ApplyProfile):
    '''DataObject representing a Distributed Virtual Switch this host is connected to.
    '''
    
    def __init__(self, key, name, uplink):
        # MUST define these
        super(DvsProfile, self).__init__()
    
        self.data['key'] = key
        self.data['name'] = name
        self.data['uplink'] = uplink
    
    
    @property
    def key(self):
        '''The linkable identifier
        '''
        return self.data['key']

    @property
    def name(self):
        '''Unique identifier for the Distributed Virtual Switch
        '''
        return self.data['name']

    @property
    def uplink(self):
        '''Mapping of PNICs to Uplinks
        '''
        return self.data['uplink']

