
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VMFSDatastoreCreatedEvent(HostEvent):
    '''This event records when a VMFS datastore is created.
    '''
    
    def __init__(self, datastore):
        # MUST define these
        super(VMFSDatastoreCreatedEvent, self).__init__()
    
        self.data['datastore'] = datastore
    
    
    @property
    def datastore(self):
        '''The associated datastore.
        '''
        return self.data['datastore']

