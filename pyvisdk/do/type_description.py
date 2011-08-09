
from pyvisdk.do.description import Description
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class TypeDescription(Description):
    '''Static strings used for describing an object type.
    '''
    
    def __init__(self, key):
        # MUST define these
        super(TypeDescription, self).__init__()
    
        self.data['key'] = key
    
    
    @property
    def key(self):
        '''Type being described
        '''
        return self.data['key']

