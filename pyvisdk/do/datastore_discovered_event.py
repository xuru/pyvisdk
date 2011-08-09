
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DatastoreDiscoveredEvent(HostEvent):
    '''This event records when a host is added to VirtualCenter and datastores are
        discovered.
    '''
    
    def __init__(self, datastore):
        # MUST define these
        super(DatastoreDiscoveredEvent, self).__init__()
    
        self.data['datastore'] = datastore
    
    
    @property
    def datastore(self):
        '''The associated datastore.
        '''
        return self.data['datastore']

