
from pyvisdk.do.description import Description
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ElementDescription(Description):
    '''Static strings used for describing an object model string or enumeration.
    '''
    
    def __init__(self, key):
        # MUST define these
        super(ElementDescription, self).__init__()
    
        self.data['key'] = key
    
    
    @property
    def key(self):
        '''Enumeration or literal ID being described.
        '''
        return self.data['key']

