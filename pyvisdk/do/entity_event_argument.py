
from pyvisdk.do.event_argument import EventArgument
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class EntityEventArgument(EventArgument):
    '''The event argument is a managed entity object.Subclasses of this type distinguish
        the different managed entities referenced in event objects.
    '''
    
    def __init__(self, name):
        # MUST define these
        super(EntityEventArgument, self).__init__()
    
        self.data['name'] = name
    
    
    @property
    def name(self):
        '''Name of the entity, including its full path from the root of the inventory.
        '''
        return self.data['name']

