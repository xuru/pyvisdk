
from pyvisdk.do.event import Event
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LockerReconfiguredEvent(Event):
    '''Locker was reconfigured to a new location.
    '''
    
    def __init__(self, newDatastore, oldDatastore):
        # MUST define these
        super(LockerReconfiguredEvent, self).__init__()
    
        self.data['newDatastore'] = newDatastore
        self.data['oldDatastore'] = oldDatastore
    
    
    @property
    def newDatastore(self):
        '''The datastore that is now used to back the locker. This field is not set if no
        datastore is currently backing the locker.
        '''
        return self.data['newDatastore']

    @property
    def oldDatastore(self):
        '''The datastore that was previously backing the locker. This field is not set if a
        datastore was not backing the locker previously.
        '''
        return self.data['oldDatastore']

