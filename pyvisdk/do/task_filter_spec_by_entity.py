
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class TaskFilterSpecByEntity(DynamicData):
    '''This data object type specifies a managed entity used to filter task history.
    '''
    
    def __init__(self, entity, recursion):
        # MUST define these
        super(TaskFilterSpecByEntity, self).__init__()
    
        self.data['entity'] = entity
        self.data['recursion'] = recursion
    
    
    @property
    def entity(self):
        '''The managed entity to which the task pertains.
        '''
        return self.data['entity']

    @property
    def recursion(self):
        '''Specification of related managed entities in the inventory hierarchy.
        '''
        return self.data['recursion']

