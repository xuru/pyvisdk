
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DatastoreRenamedOnHostEvent(HostEvent):
    '''This event records when a datastore is added to VirtualCenter and is renamed by
        VirtualCenter because this datastore already exists in VirtualCenter with
        a different name, or because the name conflicts with another datastore in
        VirtualCenter.
    '''
    
    def __init__(self, newName, oldName):
        # MUST define these
        super(DatastoreRenamedOnHostEvent, self).__init__()
    
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

