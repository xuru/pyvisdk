
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfileDescription(DynamicData):
    '''DataObject which describes the profile. Description contains multiple sections.
        Each section describes some sub-part of the profile.
    '''
    
    def __init__(self, section):
        # MUST define these
        super(ProfileDescription, self).__init__()
    
        self.data['section'] = section
    
    
    @property
    def section(self):
        '''Sections which make up the Description.
        '''
        return self.data['section']

