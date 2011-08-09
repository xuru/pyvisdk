
from pyvisdk.do.entity_event_argument import EntityEventArgument
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ManagedEntityEventArgument(EntityEventArgument):
    '''The general event argument for a managed entity.
    '''
    
    def __init__(self, entity):
        # MUST define these
        super(ManagedEntityEventArgument, self).__init__()
    
        self.data['entity'] = entity
    
    
    @property
    def entity(self):
        '''The managed entity.
        '''
        return self.data['entity']

