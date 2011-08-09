
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationSpecItem(DynamicData):
    '''Specification information and the Specification object.
    '''
    
    def __init__(self, info, spec):
        # MUST define these
        super(CustomizationSpecItem, self).__init__()
    
        self.data['info'] = info
        self.data['spec'] = spec
    
    
    @property
    def info(self):
        '''Information about the specification - name, description, and so on.
        '''
        return self.data['info']

    @property
    def spec(self):
        '''The customization specification.
        '''
        return self.data['spec']

