
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VMFSDatastoreExtendedEvent(HostEvent):
    '''This event records when a datastore is extended.
    '''
    
    def __init__(self, datastore):
        # MUST define these
        super(VMFSDatastoreExtendedEvent, self).__init__()
    
        self.data['datastore'] = datastore
    
    
    @property
    def datastore(self):
        '''The associated datastore.
        '''
        return self.data['datastore']

