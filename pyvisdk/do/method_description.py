
from pyvisdk.do.description import Description
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class MethodDescription(Description):
    '''Static strings used for describing an object model method.
    '''
    
    def __init__(self, key):
        # MUST define these
        super(MethodDescription, self).__init__()
    
        self.data['key'] = key
    
    
    @property
    def key(self):
        '''Method being described.
        '''
        return self.data['key']

