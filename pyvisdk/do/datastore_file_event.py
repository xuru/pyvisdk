
from pyvisdk.do.datastore_event import DatastoreEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DatastoreFileEvent(DatastoreEvent):
    '''Base class for events related to datastore file and directory operations.Property
        inherited from DatastoreEvent refers to the destination datastore in case
        there is more than datastore involved in the operation.
    '''
    
    def __init__(self, targetFile):
        # MUST define these
        super(DatastoreFileEvent, self).__init__()
    
        self.data['targetFile'] = targetFile
    
    
    @property
    def targetFile(self):
        '''Datastore path of the target file or directory.
        '''
        return self.data['targetFile']

