
from pyvisdk.do.datastore_event import DatastoreEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DatastoreDuplicatedEvent(DatastoreEvent):
    '''This event records when a duplicate datastore name is found. This event is used in
        VirtualCenter 1.x and is included for backward compatibility.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(DatastoreDuplicatedEvent, self).__init__()
    

    
    
