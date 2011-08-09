
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class EnumDescription(DynamicData):
    '''Static strings used for describing an enumerated type.
    '''
    
    def __init__(self, key, tags):
        # MUST define these
        super(EnumDescription, self).__init__()
    
        self.data['key'] = key
        self.data['tags'] = tags
    
    
    @property
    def key(self):
        '''Type of enumeration being described.
        '''
        return self.data['key']

    @property
    def tags(self):
        '''Element descriptions of all the tags for that enumerated type.
        '''
        return self.data['tags']

