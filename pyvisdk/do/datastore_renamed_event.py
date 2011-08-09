
from pyvisdk.do.datastore_event import DatastoreEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DatastoreRenamedEvent(DatastoreEvent):
    '''This event records the renaming of a datastore.
    '''
    
    def __init__(self, newName, oldName):
        # MUST define these
        super(DatastoreRenamedEvent, self).__init__()
    
        self.data['newName'] = newName
        self.data['oldName'] = oldName
    
    
    @property
    def newName(self):
        '''The new datastore name.
        '''
        return self.data['newName']

    @property
    def oldName(self):
        '''The old datastore name.
        '''
        return self.data['oldName']

