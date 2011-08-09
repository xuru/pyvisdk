
from pyvisdk.do.event import Event
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LockerMisconfiguredEvent(Event):
    '''Locker has not been configured properly. This event is fired when the datastore
        configured to back the locker does not exist or when connectivity to the
        datastore is lost.
    '''
    
    def __init__(self, datastore):
        # MUST define these
        super(LockerMisconfiguredEvent, self).__init__()
    
        self.data['datastore'] = datastore
    
    
    @property
    def datastore(self):
        '''The datastore that has been configured to back the locker
        '''
        return self.data['datastore']

