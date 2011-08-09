
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfileDescriptionSection(DynamicData):
    '''
    '''
    
    def __init__(self, description, message):
        # MUST define these
        super(ProfileDescriptionSection, self).__init__()
    
        self.data['description'] = description
        self.data['message'] = message
    
    
    @property
    def description(self):
        '''property describing this section.
        '''
        return self.data['description']

    @property
    def message(self):
        '''List of messages that make up the section
        '''
        return self.data['message']

