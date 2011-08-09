
from pyvisdk.do.datastore_file_event import DatastoreFileEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DatastoreFileCopiedEvent(DatastoreFileEvent):
    '''This event records copy of a file or directory.
    '''
    
    def __init__(self, sourceDatastore, sourceFile):
        # MUST define these
        super(DatastoreFileCopiedEvent, self).__init__()
    
        self.data['sourceDatastore'] = sourceDatastore
        self.data['sourceFile'] = sourceFile
    
    
    @property
    def sourceDatastore(self):
        '''Source datastore.
        '''
        return self.data['sourceDatastore']

    @property
    def sourceFile(self):
        '''Datastore path of the source file or directory.
        '''
        return self.data['sourceFile']

