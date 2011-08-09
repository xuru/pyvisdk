
from pyvisdk.do.datastore_event import DatastoreEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DatastoreCapacityIncreasedEvent(DatastoreEvent):
    '''This event records when increase in a datastore's capacity is observed. It may
        happen due to different reasons, like extending or expanding a datastore.
    '''
    
    def __init__(self, newCapacity, oldCapacity):
        # MUST define these
        super(DatastoreCapacityIncreasedEvent, self).__init__()
    
        self.data['newCapacity'] = newCapacity
        self.data['oldCapacity'] = oldCapacity
    
    
    @property
    def newCapacity(self):
        '''The new datastore capacity.
        '''
        return self.data['newCapacity']

    @property
    def oldCapacity(self):
        '''The old datastore capacity.
        '''
        return self.data['oldCapacity']

