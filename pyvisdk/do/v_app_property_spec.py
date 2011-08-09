
from pyvisdk.do.array_update_spec import ArrayUpdateSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VAppPropertySpec(ArrayUpdateSpec):
    '''An incremental update to the Property list.
    '''
    
    def __init__(self, info):
        # MUST define these
        super(VAppPropertySpec, self).__init__()
    
        self.data['info'] = info
    
    
    @property
    def info(self):
        '''
        '''
        return self.data['info']

