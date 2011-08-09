
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DatastoreRemovedOnHostEvent(HostEvent):
    '''This event records when a datastore is removed from a host but not from
        VirtualCenter.
    '''
    
    def __init__(self, datastore):
        # MUST define these
        super(DatastoreRemovedOnHostEvent, self).__init__()
    
        self.data['datastore'] = datastore
    
    
    @property
    def datastore(self):
        '''The associated datastore.
        '''
        return self.data['datastore']

