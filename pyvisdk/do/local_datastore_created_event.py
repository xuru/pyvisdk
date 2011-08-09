
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LocalDatastoreCreatedEvent(HostEvent):
    '''This event records when a local datastore is created.
    '''
    
    def __init__(self, datastore):
        # MUST define these
        super(LocalDatastoreCreatedEvent, self).__init__()
    
        self.data['datastore'] = datastore
    
    
    @property
    def datastore(self):
        '''The associated datastore.
        '''
        return self.data['datastore']

