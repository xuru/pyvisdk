
from pyvisdk.do.entity_event_argument import EntityEventArgument
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DatastoreEventArgument(EntityEventArgument):
    '''The event argument is a Datastore object.
    '''
    
    def __init__(self, datastore):
        # MUST define these
        super(DatastoreEventArgument, self).__init__()
    
        self.data['datastore'] = datastore
    
    
    @property
    def datastore(self):
        '''The Datastore object.
        '''
        return self.data['datastore']

