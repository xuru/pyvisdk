
from pyvisdk.do.array_update_spec import ArrayUpdateSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VAppOvfSectionSpec(ArrayUpdateSpec):
    '''An incremental update to the OvfSection list.
    '''
    
    def __init__(self, info):
        # MUST define these
        super(VAppOvfSectionSpec, self).__init__()
    
        self.data['info'] = info
    
    
    @property
    def info(self):
        '''
        '''
        return self.data['info']

