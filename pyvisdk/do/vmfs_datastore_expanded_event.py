
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VMFSDatastoreExpandedEvent(HostEvent):
    '''This event records when a datastore is expanded.
    '''
    
    def __init__(self, datastore):
        # MUST define these
        super(VMFSDatastoreExpandedEvent, self).__init__()
    
        self.data['datastore'] = datastore
    
    
    @property
    def datastore(self):
        '''The associated datastore.
        '''
        return self.data['datastore']

