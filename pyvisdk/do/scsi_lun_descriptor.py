
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ScsiLunDescriptor(DynamicData):
    '''A structure that encapsulates an identifier and its properties for the ScsiLun
        object.
    '''
    
    def __init__(self, id, quality):
        # MUST define these
        super(ScsiLunDescriptor, self).__init__()
    
        self.data['id'] = id
        self.data['quality'] = quality
    
    
    @property
    def id(self):
        '''The identifier represented as a string.
        '''
        return self.data['id']

    @property
    def quality(self):
        '''An indicator of the utility of the descriptor as an identifier that is stable,
        unique, and correlatable.
        '''
        return self.data['quality']

