
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class EventFilterSpecByEntity(DynamicData):
    '''This option specifies a managed entity used to filter event history. If the
        specified managed entity is a Folder or a ResourcePool, the query will
        actually be performed on the entities contained within that Folder or
        ResourcePool, so you cannot query for events on Folders and ResourcePools
        themselves this way.
    '''
    
    def __init__(self, entity, recursion):
        # MUST define these
        super(EventFilterSpecByEntity, self).__init__()
    
        self.data['entity'] = entity
        self.data['recursion'] = recursion
    
    
    @property
    def entity(self):
        '''The managed entity to which the event pertains.
        '''
        return self.data['entity']

    @property
    def recursion(self):
        '''Specification of related managed entities in the inventory hierarchy.
        '''
        return self.data['recursion']

