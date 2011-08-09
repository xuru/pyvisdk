
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class Tag(DynamicData):
    '''Defines a tag that can be associated with a managed entity.
    '''
    
    def __init__(self, key):
        # MUST define these
        super(Tag, self).__init__()
    
        self.data['key'] = key
    
    
    @property
    def key(self):
        '''The tag key in human readable form.
        '''
        return self.data['key']

