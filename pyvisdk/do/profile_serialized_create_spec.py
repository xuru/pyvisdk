
from pyvisdk.do.profile_create_spec import ProfileCreateSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfileSerializedCreateSpec(ProfileCreateSpec):
    '''DataObject describing the profile in a string serialized representation.
    '''
    
    def __init__(self, profileConfigString):
        # MUST define these
        super(ProfileSerializedCreateSpec, self).__init__()
    
        self.data['profileConfigString'] = profileConfigString
    
    
    @property
    def profileConfigString(self):
        '''Represenation of the profile in the string form
        '''
        return self.data['profileConfigString']

